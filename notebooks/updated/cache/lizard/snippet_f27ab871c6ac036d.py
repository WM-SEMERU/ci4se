def train(self, net_sizes, epochs, batchsize):
    self.trainer = ClassificationTrainer(self.data, self.targets, net_sizes)
    self.trainer.learn(epochs, batchsize)
    return self.trainer.evaluate(batchsize)