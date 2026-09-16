def _ParseFileEntry(self, knowledge_base, file_entry):
    file_object = file_entry.GetFileObject()
    try:
        self._ParseFileData(knowledge_base, file_object)
    finally:
        file_object.close()