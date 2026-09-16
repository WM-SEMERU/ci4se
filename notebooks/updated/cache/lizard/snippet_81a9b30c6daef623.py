def recall(self, label=None):
    if label is None:
        return self.call('recall')
    else:
        return self.call('recall', float(label))