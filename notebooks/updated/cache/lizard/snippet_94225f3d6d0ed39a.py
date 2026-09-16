def annotate(self, word, pos=None, polarity=0.0, subjectivity=0.0,
    intensity=1.0, label=None):
    w = self.setdefault(word, {})
    w[pos] = w[None] = polarity, subjectivity, intensity
    if label:
        self.labeler[word] = label