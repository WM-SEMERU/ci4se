def compare_sentences(self, str_a, str_b, language):
    sents_a = []
    sents_b = []
    ratios = []
    if language == 'latin':
        sent_tokenizer = TokenizeSentence('latin')
    elif language == 'greek':
        sent_tokenizer = TokenizeSentence('greek')
    else:
        print(
            "Language for sentence tokenization not recognized. Accepted values are 'latin' and 'greek'."
            )
        return
    if self.stem_words:
        stemmer = Stemmer()
        str_a = stemmer.stem(str_a)
        str_b = stemmer.stem(str_b)
    sents_a = sent_tokenizer.tokenize_sentences(str_a)
    sents_b = sent_tokenizer.tokenize_sentences(str_b)
    sents_a = self._process_sentences(sents_a)
    sents_b = self._process_sentences(sents_b)
    comparisons = self._calculate_ratios(sents_a, sents_b)
    return comparisons