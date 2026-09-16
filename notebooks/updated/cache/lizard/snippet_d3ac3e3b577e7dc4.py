def extract_phrases(self, text):
    analysis = self.analyze(text)
    for pos1 in range(len(analysis)):
        rec1 = analysis[pos1]
        if not self.is_stopword_record(rec1):
            yield self.get_record_root(rec1), rec1[0]
            for pos2 in range(pos1 + 1, len(analysis)):
                rec2 = analysis[pos2]
                if not self.is_stopword_record(rec2):
                    roots = [self.get_record_root(rec1), self.
                        get_record_root(rec2)]
                    pieces = [analysis[i][0] for i in range(pos1, pos2 + 1)]
                    term = ' '.join(roots)
                    phrase = ''.join(pieces)
                    yield term, phrase
                    break