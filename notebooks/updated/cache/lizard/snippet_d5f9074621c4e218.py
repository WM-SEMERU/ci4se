def find_column(self, token):
    i = token.lexpos
    while i > 0:
        if self.input_data[i - 1] == '\n':
            break
        i -= 1
    column = token.lexpos - i + 1
    return column