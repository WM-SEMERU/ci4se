def encode_sentences(sentences, vocab=None, invalid_label=-1, invalid_key=
    '\n', start_label=0, unknown_token=None):
    idx = start_label
    if vocab is None:
        vocab = {invalid_key: invalid_label}
        new_vocab = True
    else:
        new_vocab = False
    res = []
    for sent in sentences:
        coded = []
        for word in sent:
            if word not in vocab:
                assert new_vocab or unknown_token, 'Unknown token %s' % word
                if idx == invalid_label:
                    idx += 1
                if unknown_token:
                    word = unknown_token
                vocab[word] = idx
                idx += 1
            coded.append(vocab[word])
        res.append(coded)
    return res, vocab