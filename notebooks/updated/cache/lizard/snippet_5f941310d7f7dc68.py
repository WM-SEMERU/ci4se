def build(self):
    if self._category_text_iter is None:
        raise CategoryTextIterNotSetError()
    nlp = self.get_nlp()
    category_document_iter = ((category, self._clean_function(raw_text)) for
        category, raw_text in self._category_text_iter)
    term_doc_matrix = self._build_from_category_spacy_doc_iter((category,
        nlp(text)) for category, text in category_document_iter if text.
        strip() != '')
    return term_doc_matrix