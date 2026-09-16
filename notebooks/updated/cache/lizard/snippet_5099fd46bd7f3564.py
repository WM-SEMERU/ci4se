def train(self, data, label, batch_size):
    sum_losses = 0
    len_losses = 0
    with autograd.record():
        losses = [self.loss_fn(self.net(X), Y) for X, Y in zip(data, label)]
    for loss in losses:
        sum_losses += mx.nd.array(loss).sum().asscalar()
        len_losses += len(loss)
        loss.backward()
    self.trainer.step(batch_size)
    return sum_losses, len_losses