def set_terms(self, *terms, **kw_terms):
    for t in terms:
        self.add_term(t)
    for k, v in kw_terms.items():
        try:
            value, props = v
        except (ValueError, TypeError) as e:
            value, props = v, {}
        self.new_term(k, value, **props)