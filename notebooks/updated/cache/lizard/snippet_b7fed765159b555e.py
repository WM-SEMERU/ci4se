def setEditorData(self, editor, index):
    data = unwrapVariant(index.data())
    editor.setCurrentIndex(editor.findText(data))