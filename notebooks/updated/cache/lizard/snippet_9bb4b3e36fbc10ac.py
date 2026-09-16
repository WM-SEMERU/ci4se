def _onShortcutPrint(self):
    dialog = QPrintDialog(self)
    if dialog.exec_() == QDialog.Accepted:
        printer = dialog.printer()
        self.print_(printer)