def train_cb(self, param):
    if param.nbatch % self.frequent == 0:
        self._process_batch(param, 'train')