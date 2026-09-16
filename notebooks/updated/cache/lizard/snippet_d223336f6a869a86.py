def setModelData(self, editor, model, index):
    editor.saveToObject()
    model.dataEdited()
    editor.attributesSaved.disconnect()
    if hasattr(editor, 'vocalFilesChanged'):
        editor.vocalFilesChanged.disconnect()
    editor.close()