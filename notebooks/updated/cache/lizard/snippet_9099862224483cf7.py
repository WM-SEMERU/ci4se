def set_learning_rate(self, lr):
    if not isinstance(self._optimizer, opt.Optimizer):
        raise UserWarning(
            'Optimizer has to be defined before its learning rate is mutated.')
    else:
        self._optimizer.set_learning_rate(lr)