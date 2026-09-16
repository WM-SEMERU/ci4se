def setEditorData(self, editor, index):
    text = from_qvariant(index.model().data(index, Qt.DisplayRole), str)
    editor.setText(text)