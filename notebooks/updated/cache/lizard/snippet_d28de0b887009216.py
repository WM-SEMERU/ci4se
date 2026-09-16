def showMessage(self, message, *args):
    QSplashScreen.showMessage(self, message, Qt.AlignBottom | Qt.AlignRight |
        Qt.AlignAbsolute, QColor(Qt.white))