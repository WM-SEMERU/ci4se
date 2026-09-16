def sentences(self):
    sents = []
    spans = self.sentence_tokenizer.span_tokenize(self.text)
    for span in spans:
        sent = Sentence(text=self.text[span[0]:span[1]], start=span[0], end
            =span[1], word_tokenizer=self.word_tokenizer, lexicon=self.
            lexicon, abbreviation_detector=self.abbreviation_detector,
            pos_tagger=self.pos_tagger, ner_tagger=self.ner_tagger, parsers
            =self.parsers, document=self.document)
        sents.append(sent)
    return sents