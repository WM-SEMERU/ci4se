def get_texts(self):
    with self.getstream() as text_stream:
        for i, line in enumerate(text_stream):
            line = to_unicode(line)
            line = (TweetCorpus.case_normalizer or passthrough)(line)
            if self.mask is not None and not self.mask[i]:
                continue
            ngrams = []
            for ng in tokens2ngrams((TweetCorpus.tokenizer or str.split)(
                line), n=self.num_grams):
                if self.ignore_matcher(ng):
                    continue
                ngrams += [ng]
            if not i % 1000:
                print(line)
                print(ngrams)
            yield ngrams