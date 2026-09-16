def evaluate_inline_tail(self, groups):
    if self.lines:
        self.line_comments.append([groups['line'][2:].replace('\\\n', ''),
            self.line_num, self.current_encoding])