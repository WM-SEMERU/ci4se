def learn_batch(self, inputBatch):
    X = inputBatch
    Y = self.encode_batch(X)
    self.update_statistics(Y)
    self.update_weights(X, Y)
    return Y