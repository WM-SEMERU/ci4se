def in_global_expression(self):
    return (self.parenthesis_count == 0 and self.curly_bracket_count == 0 and
        self.square_bracket_count == 0 and not self.in_single_quote and not
        self.in_double_quote)