def tokenize(self, unicode_sentence, mode='default', HMM=True):
    if not isinstance(unicode_sentence, text_type):
        raise ValueError('jieba: the input parameter should be unicode.')
    start = 0
    if mode == 'default':
        for w in self.cut(unicode_sentence, HMM=HMM):
            width = len(w)
            yield w, start, start + width
            start += width
    else:
        for w in self.cut(unicode_sentence, HMM=HMM):
            width = len(w)
            if len(w) > 2:
                for i in xrange(len(w) - 1):
                    gram2 = w[i:i + 2]
                    if self.FREQ.get(gram2):
                        yield gram2, start + i, start + i + 2
            if len(w) > 3:
                for i in xrange(len(w) - 2):
                    gram3 = w[i:i + 3]
                    if self.FREQ.get(gram3):
                        yield gram3, start + i, start + i + 3
            yield w, start, start + width
            start += width