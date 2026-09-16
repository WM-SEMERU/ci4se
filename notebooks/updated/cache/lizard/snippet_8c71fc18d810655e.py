def _invalid_string_quote(self, quote, row, correct_quote=None, col=None):
    if not correct_quote:
        correct_quote = SMART_QUOTE_OPTS.get(self.config.string_quote)
    self.add_message('invalid-string-quote', line=row, args=(quote,
        correct_quote), **self.get_offset(col))