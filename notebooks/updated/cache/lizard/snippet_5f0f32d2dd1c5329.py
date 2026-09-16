def get_term_frequency(self, term, document, normalized=False):
    if document not in self._documents:
        raise IndexError(DOCUMENT_DOES_NOT_EXIST)
    if term not in self._terms:
        raise IndexError(TERM_DOES_NOT_EXIST)
    result = self._terms[term].get(document, 0)
    if normalized:
        result /= self.get_document_length(document)
    return float(result)