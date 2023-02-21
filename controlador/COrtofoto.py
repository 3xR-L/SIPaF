from modelo.Ortofoto import Ortofoto
import os
from shutil import copyfile
from exif import Image
import cv2


def gsd(height, sensor_height, sensor_width, focal_length, image_height, image_width):
    gsd_w = (height * sensor_width) / (focal_length * image_width)
    gsd_h = (height * sensor_height) / (focal_length * image_height)
    return gsd_w * 100, gsd_h * 100

class COrtofoto:
    def __init__(self, dirEDT, ortofoto = None):
        self.dirIma = dirEDT+ '/Imagenes'
        self.dirEDT = dirEDT
        self.ortofoto = ortofoto

    def preprocesarImagenes(self, dirImagenes, Camaras, altura):
        # Copy the images to the thermal folder of the project
        dirImag = os.listdir(dirImagenes)
        for image in dirImag:
            # check the image extension and size
            if (image.endswith('.jpg') or image.endswith('.png') or image.endswith('jpeg')) and os.path.getsize(dirImagenes + '/' + image) < 1000000:
                # copy the image to the thermal folder
                copyfile(dirImagenes + '/' + image, self.dirIma + '/IR/originales/' + image)
            elif(image.endswith('.jpg') or image.endswith('.png') or image.endswith('jpeg')) and os.path.getsize(dirImagenes + '/' + image) > 1000000:
                # preprocess image before copying with opencv
                xt2Vis_w, xt2Vis_h = gsd(height=altura, sensor_height=Camaras[0].alturaSensor, sensor_width=Camaras[0].anchoSensor, focal_length=Camaras[0].largoFocal,
                                         image_height=Camaras[0].alturaPixeles, image_width=Camaras[0].anchoPixeles)
                xt2Inf_w, xt2Inf_h = gsd(height=altura, sensor_height=Camaras[1].alturaSensor, sensor_width=Camaras[1].anchoSensor, focal_length=Camaras[1].largoFocal,
                                         image_height=Camaras[1].alturaPixeles, image_width=Camaras[1].anchoPixeles)
                correction_width = round((xt2Vis_w * ((640 * xt2Inf_w) / xt2Vis_h)) / 2)
                correction_height = round((xt2Vis_h * ((512 * xt2Inf_h) / xt2Vis_h)) / 2)
                # calculate the center of the image
                left = (Camaras[0].anchoPixeles / 2) - correction_width
                top = (Camaras[0].alturaPixeles / 2) - correction_height
                right = (Camaras[0].anchoPixeles / 2) + correction_width
                bottom = (Camaras[0].alturaPixeles / 2) + correction_height

                # # read the image with cv2
                img = cv2.imread(dirImagenes + '/' + image)

                # crop the image
                img = img[int(top):int(bottom), int(left):int(right)]

                # save the image
                cv2.imwrite(self.dirIma + '/RGB/originales/' + image, img)


