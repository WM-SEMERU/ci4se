def setModelData(self, editor, model, index):
    value = editor.currentText()
    model.setData(index, wrapVariant(value))