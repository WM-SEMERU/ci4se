def tokenize(self, text, include_punc=True, **kwargs):
    return self.tokenizer.word_tokenize(text, include_punc, **kwargs)