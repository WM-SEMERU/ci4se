def _opening_bracket_index(self, text, bpair=('(', ')')):
    level = 1
    for i, char in enumerate(reversed(text[:-1])):
        if char == bpair[1]:
            level += 1
        elif char == bpair[0]:
            level -= 1
        if level == 0:
            return len(text) - i - 2