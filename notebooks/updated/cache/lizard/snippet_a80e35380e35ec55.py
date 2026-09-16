def parse(self, sentence):
    words = np.zeros((len(sentence) + 1, 1), np.int32)
    tags = np.zeros((len(sentence) + 1, 1), np.int32)
    words[0, 0] = ParserVocabulary.ROOT
    tags[0, 0] = ParserVocabulary.ROOT
    vocab = self._vocab
    for i, (word, tag) in enumerate(sentence):
        words[i + 1, 0], tags[i + 1, 0] = vocab.word2id(word.lower()
            ), vocab.tag2id(tag)
    with mx.Context(mxnet_prefer_gpu()):
        outputs = self._parser.forward(words, tags)
    words = []
    for arc, rel, (word, tag) in zip(outputs[0][0], outputs[0][1], sentence):
        words.append(ConllWord(id=len(words) + 1, form=word, pos=tag, head=
            arc, relation=vocab.id2rel(rel)))
    return ConllSentence(words)