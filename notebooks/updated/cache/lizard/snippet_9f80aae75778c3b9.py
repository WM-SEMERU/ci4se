def _clean_str(self, s):
    return s.translate(str.maketrans('', '', punctuation)).replace('\u200b',
        ' ').strip().lower()