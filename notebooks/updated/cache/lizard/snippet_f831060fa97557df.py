def copy(self):
    data = QMimeData()
    text = '\n'.join([cursor.selectedText() for cursor in self.cursors()])
    data.setText(text)
    data.setData(self.MIME_TYPE, text.encode('utf8'))
    QApplication.clipboard().setMimeData(data)