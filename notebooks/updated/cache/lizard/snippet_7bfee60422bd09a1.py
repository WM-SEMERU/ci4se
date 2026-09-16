def learn(self, numEpochs, batchsize):
    for epoch in range(numEpochs):
        print('epoch %d' % epoch)
        indexes = np.random.permutation(self.trainsize)
        for i in range(0, self.trainsize, batchsize):
            x = Variable(self.x_train[indexes[i:i + batchsize]])
            t = Variable(self.y_train[indexes[i:i + batchsize]])
            self.optimizer.update(self.model, x, t)