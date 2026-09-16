def escape(self, escape_func, quote_func=quote_spaces):
    if self.is_literal():
        return escape_func(self.data)
    elif ' ' in self.data or '\t' in self.data:
        return quote_func(self.data)
    else:
        return self.data