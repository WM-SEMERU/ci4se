def doc2id(self, doc):
    doc = map(self.process_token, doc)
    return [self.token_to_id(token) for token in doc]