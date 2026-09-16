def forward(self, data_batch, is_train=None):
    self._scores = data_batch.data[0]
    if is_train is None:
        is_train = self.for_training
    if is_train:
        self._labels = data_batch.label[0]