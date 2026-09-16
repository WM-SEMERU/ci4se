def get_phrase_texts(self, text, np_labels):
    phrases = self.get_phrases(text, np_labels)
    texts = []
    for phrase in phrases:
        phrase_str = ' '.join([word[TEXT] for word in phrase])
        texts.append(phrase_str)
    return texts