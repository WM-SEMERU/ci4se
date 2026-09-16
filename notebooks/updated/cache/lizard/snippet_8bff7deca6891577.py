def apply(self, word, ctx=None):
    chars = get_letters(word)
    flag = True
    reason = None
    prev_letter = None
    for char in chars:
        if prev_letter == char:
            flag = False
            break
        prev_letter = char
    if not flag:
        reason = RepeatedLetters.reason
    return flag, reason