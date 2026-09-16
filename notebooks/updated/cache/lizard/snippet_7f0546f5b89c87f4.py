def copy(self):
    text = []
    for item in self.selectedItems():
        text.append(nativestring(item.text()))
    QApplication.clipboard().setText(','.join(text))