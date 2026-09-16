def _preview(self):
    from PyQt5 import QtWidgets
    app = QtWidgets.QApplication([self._ui_file])
    widget = loadUi(self._ui_file)
    widget.show()
    return app.exec_()