def _clean_text(self, text):
    output = []
    for char in text:
        cp = ord(char)
        if cp in (0, 65533) or self._is_control(char):
            continue
        if self._is_whitespace(char):
            output.append(' ')
        else:
            output.append(char)
    return ''.join(output)