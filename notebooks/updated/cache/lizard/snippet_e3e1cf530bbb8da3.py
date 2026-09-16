def extract_terms(self, nb):
    emt = ExtractMetatabTerms()
    emt.preprocess(nb, {})
    return emt.terms