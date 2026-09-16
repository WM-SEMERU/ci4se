def find_previous_word_ending(self, count=1, WORD=False):
    if count < 0:
        return self.find_next_word_ending(count=-count, WORD=WORD)
    text_before_cursor = self.text_after_cursor[:1] + self.text_before_cursor[:
        :-1]
    regex = _FIND_BIG_WORD_RE if WORD else _FIND_WORD_RE
    iterator = regex.finditer(text_before_cursor)
    try:
        for i, match in enumerate(iterator):
            if i == 0 and match.start(1) == 0:
                count += 1
            if i + 1 == count:
                return -match.start(1) + 1
    except StopIteration:
        pass