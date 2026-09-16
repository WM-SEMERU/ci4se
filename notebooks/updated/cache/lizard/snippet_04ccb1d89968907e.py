def _count_words(self, to_lower=True, delimiters=['\r', '\x0b', '\n',
    '\x0c', '\t', ' ']):
    if self.dtype != str:
        raise TypeError(
            'Only SArray of string type is supported for counting bag of words'
            )
    if not all([(len(delim) == 1) for delim in delimiters]):
        raise ValueError('Delimiters must be single-character strings')
    options = dict()
    options['to_lower'] = to_lower == True
    options['delimiters'] = delimiters
    with cython_context():
        return SArray(_proxy=self.__proxy__.count_bag_of_words(options))