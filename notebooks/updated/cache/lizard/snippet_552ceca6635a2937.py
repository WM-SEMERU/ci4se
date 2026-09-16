def has_end(self, stream):
    for token in self.end_tokens:
        if not self.has_next(token, stream):
            continue
        offset = len(token)
        if self.has_eof(stream, offset):
            return True
        if self.has_whitespace(stream, offset):
            return True
        if self.has_comment(stream, offset):
            return True
        if self.has_next(self.statement_delimiter, stream, offset):
            return True
    return self.has_eof(stream)