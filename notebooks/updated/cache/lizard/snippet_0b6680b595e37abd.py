def compute(self):
    wordlist = self.wordlist
    xsections = {}
    for i in range(len(wordlist)):
        word_i = wordlist[i]
        for j in range(len(wordlist)):
            word_j = wordlist[j]
            if i == j:
                if not xsections.get(word_i, None):
                    xsections[word_i] = ['']
                else:
                    xsections[word_i].extend([''])
                continue
            if i > j:
                xsec_counts = xsections[word_j][i]
            else:
                xsec_counts = tamil.utf8.word_intersection(word_i, word_j)
            if not xsections.get(word_i, None):
                xsections[word_i] = [xsec_counts]
            else:
                xsections[word_i].extend([xsec_counts])
    self.xsections = xsections