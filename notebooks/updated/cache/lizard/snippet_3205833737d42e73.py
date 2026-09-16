def replace_suffixes_4(self, word):
    length = len(word)
    replacements = {'ational': 'ate', 'tional': 'tion', 'alize': 'al',
        'icate': 'ic', 'iciti': 'ic', 'ical': 'ic', 'ful': '', 'ness': ''}
    for suffix in replacements.keys():
        if word.endswith(suffix):
            suffix_length = len(suffix)
            if self.r1 <= length - suffix_length:
                word = word[:-suffix_length] + replacements[suffix]
    if word.endswith('ative'):
        if self.r1 <= length - 5 and self.r2 <= length - 5:
            word = word[:-5]
    return word