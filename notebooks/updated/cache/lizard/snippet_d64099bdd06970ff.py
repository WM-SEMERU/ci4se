def compare(self, other):
    self._validate_compare_parameters(other=other)
    return_list = []
    for idx, digit in enumerate(other):
        dwa = DigitWordAnalysis(index=idx, digit=digit, match=digit == self
            ._word[idx], in_word=self._word.count(digit) > 0, multiple=self
            ._word.count(digit) > 1)
        return_list.append(dwa)
    return return_list