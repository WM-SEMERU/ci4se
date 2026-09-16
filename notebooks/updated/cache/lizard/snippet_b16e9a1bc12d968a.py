def edit_distance_1(self, word):
    word = word.lower()
    if self._check_if_should_check(word) is False:
        return {word}
    letters = self._word_frequency.letters
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [(L + R[1:]) for L, R in splits if R]
    transposes = [(L + R[1] + R[0] + R[2:]) for L, R in splits if len(R) > 1]
    replaces = [(L + c + R[1:]) for L, R in splits if R for c in letters]
    inserts = [(L + c + R) for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)