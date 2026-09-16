def add_inspire_categories(self, subject_terms, source=None):
    for category in subject_terms:
        category_dict = self._sourced_dict(source, term=category)
        self._append_to('inspire_categories', category_dict)