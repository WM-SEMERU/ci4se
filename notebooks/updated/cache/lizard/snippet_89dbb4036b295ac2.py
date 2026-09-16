def get_documents(self, term):
    if term not in self._terms:
        raise IndexError(TERM_DOES_NOT_EXIST)
    else:
        return self._terms[term]