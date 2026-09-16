def init_encoders(self, config=DataConfig()):
    self.log('info', 'Initializing the encoders ...')
    self.ie = LabelEncoder()
    self.ie_vocab = self.ie.fit_transform(self.vocab_list)