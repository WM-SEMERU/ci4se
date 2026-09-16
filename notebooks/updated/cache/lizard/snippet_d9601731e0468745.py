def evaluate(self, batchsize):
    sum_loss, sum_accuracy = 0, 0
    for i in range(0, self.testsize, batchsize):
        x = Variable(self.x_test[i:i + batchsize])
        y = Variable(self.y_test[i:i + batchsize])
        loss = self.model(x, y)
        sum_loss += loss.data * batchsize
        sum_accuracy += self.model.accuracy.data * batchsize
    return sum_loss / self.testsize, sum_accuracy / self.testsize