def add_documents(self, documents):
    result, errors = [], []
    for document in documents:
        try:
            result.append(self.add_document(document))
        except RuntimeError as exc:
            errors.append((document, exc))
    return result, errors