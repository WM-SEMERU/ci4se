def tokenize_words(self):
    if not self.is_tagged(SENTENCES):
        self.tokenize_sentences()
    tok = self.__word_tokenizer
    text = self.text
    dicts = []
    for sentence in self[SENTENCES]:
        sent_start, sent_end = sentence[START], sentence[END]
        sent_text = text[sent_start:sent_end]
        spans = tok.span_tokenize(sent_text)
        for start, end in spans:
            dicts.append({START: start + sent_start, END: end + sent_start,
                TEXT: sent_text[start:end]})
    self[WORDS] = dicts
    return self