from modelo.Ortofoto import Ortofoto
import os
from shutil import copyfile
from exif import Image
import cv2
from PIL import Image as ImagePIL
from bs4 import BeautifulSoup


def gsd(height, sensor_height, sensor_width, focal_length, image_height, image_width):
    gsd_w = (height * sensor_width) / (focal_length * image_width)
    gsd_h = (height * sensor_height) / (focal_length * image_height)
    return gsd_w * 100, gsd_h * 100

class COrtofoto:
    def __init__(self, dirEDT, ortofoto = None):
        self.dirIma = dirEDT+ '/Imagenes'
        self.dirEDT = dirEDT
        self.ortofoto = ortofoto

    def preprocesarImagenes(self, dirImagenes, Camaras, altura, overlapVertical, overlapHorizontal):
        # Copy the images to the thermal folder of the project
        dirImag = os.listdir(dirImagenes)
        if overlapVertical <= 30:
            overlapVertical = 0
        else:
            overlapVertical = ((overlapVertical-30)/2) / 100

        if overlapHorizontal <= 30:
            overlapHorizontal = 0
        else:
            overlapHorizontal = ((overlapHorizontal-30)/2) / 100

        gimbalYawDegrees = []
        try:
            xt2Vis_w, xt2Vis_h = gsd(height=altura, sensor_height=Camaras[0].alturaSensor,
                                     sensor_width=Camaras[0].anchoSensor, focal_length=Camaras[0].largoFocal,
                                     image_height=Camaras[0].alturaPixeles, image_width=Camaras[0].anchoPixeles)
            xt2Inf_w, xt2Inf_h = gsd(height=altura, sensor_height=Camaras[1].alturaSensor,
                                     sensor_width=Camaras[1].anchoSensor, focal_length=Camaras[1].largoFocal,
                                     image_height=Camaras[1].alturaPixeles, image_width=Camaras[1].anchoPixeles)

            correction_width = (xt2Inf_w / xt2Vis_w * Camaras[1].anchoPixeles) / 4
            correction_height = (xt2Inf_h / xt2Vis_h * Camaras[1].alturaPixeles) / 4

            for image in dirImag:
                with open(dirImagenes + '/' + image, "rb") as fin:
                    img = fin.read()
                    imgAsString = str(img)
                    xmp_start = imgAsString.find('<x:xmpmeta')
                    xmp_end = imgAsString.find('</x:xmpmeta')
                    if xmp_start != xmp_end:
                        xmpString = imgAsString[xmp_start:xmp_end + 12]
                    xmpAsXML = BeautifulSoup(xmpString, features="lxml")

                    # Extract the <drone-dji:gimbalyawdegree> tag
                    gimbalYawDegree = xmpAsXML.find('drone-dji:gimbalyawdegree')
                    # separate the tag from the value
                    gimbalYawDegree = str(gimbalYawDegree).split('>')[1].split('<')[0]
                    gimbalYawDegrees.append(gimbalYawDegree)

                # check the image extension and size
                if (image.endswith('.jpg') or image.endswith('.png') or image.endswith('jpeg')) and os.path.getsize(dirImagenes + '/' + image) < 1000000:
                    # crop the image to the perccentage of overlaps
                    # read the image with cv2
                    img = ImagePIL.open(dirImagenes + '/' + image)
                    exif = img.getexif()

                    width_before, height_before = img.size

                    # get the image size
                    width, height = img.width, img.height

                    # calculate the center of the image
                    left = width * overlapVertical
                    top = height * overlapHorizontal
                    right = width - left
                    bottom = height - top

                    # crop the image
                    img = img.crop((int(left), int(top), int(right), int(bottom)))

                    # rotate image based on the gimbal yaw degree
                    img = img.rotate(float(gimbalYawDegree) * -1, expand=True)

                    # save the cropped image with its metadata
                    img.save(self.dirIma + '/IR/originales/' + image, exif=exif)

                elif(image.endswith('.jpg') or image.endswith('.png') or image.endswith('jpeg')) and os.path.getsize(dirImagenes + '/' + image) > 1000000:
                    # preprocess image before copying with opencv
                    try:
                        # # read the image with cv2
                        image_exif = ImagePIL.open(dirImagenes + '/' + image)
                        exif = image_exif.getexif()

                        # calculate the center of the image
                        left = (image_exif.width / 2) - correction_width
                        top = (image_exif.height / 2) - correction_height
                        right = (image_exif.width / 2) + correction_width
                        bottom = (image_exif.height / 2) + correction_height

                        # crop the image to fit the thermal image
                        img = image_exif.crop((int(left), int(top), int(right), int(bottom)))

                        # crop the image to the perccentage of overlaps and get the image size
                        width, height = img.size

                        # # calculate the center of the image
                        left = width * (overlapVertical+0.035)
                        top = height * (overlapHorizontal+0.035)
                        right = width - left
                        bottom = height - top

                        # # crop the image
                        img = img.crop((int(left), int(top), int(right), int(bottom)))

                        # rotate image based on the gimbal yaw degree
                        img = img.rotate(float(gimbalYawDegree) * -1, expand=True)

                        # save the cropped image with its metadata
                        img.save(self.dirIma + '/REl GB/originales/' + image, exif=exif)

                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)
