def vectorize_utterance_ohe(self, utterance):
    for i, word in enumerate(utterance):
        if not word in self.vocab_list:
            utterance[i] = '<unk>'
    ie_utterance = self.swap_pad_and_zero(self.ie.transform(utterance))
    ohe_utterance = np.array(self.ohe.transform(ie_utterance.reshape(len(
        ie_utterance), 1)))
    return ohe_utterance