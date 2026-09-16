def load_document(self, document, file=None, language=None):
    document.setDocumentLayout(QPlainTextDocumentLayout(document))
    self.setDocument(document)
    self.set_file(file)
    self.set_language(language)
    self.__set_document_signals()
    self.file_loaded.emit()
    return True