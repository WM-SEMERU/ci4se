def check_all(self):
    self.file_errors = 0
    self.line_number = 0
    self.indent_char = None
    self.indent_level = 0
    self.previous_logical = ''
    self.blank_lines = 0
    self.tokens = []
    parens = 0
    for token in tokenize.generate_tokens(self.readline_check_physical):
        self.tokens.append(token)
        token_type, text = token[0:2]
        if token_type == tokenize.OP and text in '([{':
            parens += 1
        if token_type == tokenize.OP and text in '}])':
            parens -= 1
        if token_type == tokenize.NEWLINE and not parens:
            self.check_logical()
            self.blank_lines = 0
            self.tokens = []
        if token_type == tokenize.NL and not parens:
            if len(self.tokens) <= 1:
                self.blank_lines += 1
            self.tokens = []
        if token_type == tokenize.COMMENT:
            source_line = token[4]
            token_start = token[2][1]
            if source_line[:token_start].strip() == '':
                self.blank_lines = 0
            if text.endswith('\n') and not parens:
                self.tokens = []
    return self.file_errors