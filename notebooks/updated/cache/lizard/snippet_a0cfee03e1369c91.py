def _make_query_from_terms(self, terms):
    expanded_terms = self._expand_terms(terms)
    cterms = ''
    if expanded_terms['doc']:
        cterms = self.backend._or_join(expanded_terms['doc'])
    keywords = expanded_terms['keywords']
    frm_to = self._from_to_as_term(expanded_terms['from'], expanded_terms['to']
        )
    if frm_to:
        keywords.append(frm_to)
    if keywords:
        if cterms:
            cterms = self.backend._and_join([cterms, self.backend.
                _field_term('keywords', expanded_terms['keywords'])])
        else:
            cterms = self.backend._field_term('keywords', expanded_terms[
                'keywords'])
    logger.debug(
        'partition terms conversion: `{}` terms converted to `{}` query.'.
        format(terms, cterms))
    return cterms