def _load_words(self):
    with open(self._words_file, 'r') as f:
        self._censor_list = [line.strip() for line in f.readlines()]