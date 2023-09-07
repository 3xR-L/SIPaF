"""Módulo principal de la aplicación."""

import sys

from PyQt5 import QtWidgets as qtw
from controlador.CEDT import CEDT


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    ui = CEDT()
    if ui.CGEDT.mEDT is not None:
        ui.showMaximized()
        sys.exit(app.exec_())
