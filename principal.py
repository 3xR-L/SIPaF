from controlador.CEDT import CEDT

from PyQt5 import QtWidgets as qtw
import sys

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    ui = CEDT()
    if ui.CGEDT.mEDT is not None:
        ui.showMaximized()
        sys.exit(app.exec_())
