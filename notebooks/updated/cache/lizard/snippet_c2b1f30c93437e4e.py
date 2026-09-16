def add_loss(self, loss, name=None, regularization=False, add_summaries=True):
    _ = name
    if regularization:
        self._g.add_to_collection(GraphKeys.REGULARIZATION_LOSSES, loss)
    tf.add_to_collection(GraphKeys.LOSSES, loss)
    if add_summaries:
        self.add_scalar_summary(loss, 'loss')
        self.add_average_summary(loss, 'loss_average')