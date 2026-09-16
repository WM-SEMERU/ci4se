def text_after(self, start, match_on):
    text = ''
    index = start - 1
    while index > 0:
        text = self.code[index:start]
        if text.startswith(match_on):
            return text.lstrip(match_on)
        index -= 1
    return text.lstrip(match_on)