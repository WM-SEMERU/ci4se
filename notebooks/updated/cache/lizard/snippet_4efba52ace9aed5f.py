def describe(self: object, fileids: str=None):
    started = time.time()
    counts = FreqDist()
    tokens = FreqDist()
    for para in self.paras(fileids):
        counts['paras'] += 1
        for sent in para:
            counts['sents'] += 1
            for word in sent:
                counts['words'] += 1
                tokens[word] += 1
    n_fileids = len(self.fileids())
    return {'files': n_fileids, 'paras': counts['paras'], 'sents': counts[
        'sents'], 'words': counts['words'], 'vocab': len(tokens), 'lexdiv':
        round(counts['words'] / len(tokens), 3), 'ppdoc': round(counts[
        'paras'] / n_fileids, 3), 'sppar': round(counts['sents'] / counts[
        'paras'], 3), 'secs': round(time.time() - started, 3)}