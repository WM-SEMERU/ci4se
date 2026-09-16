def backward(self, loss):
    with mx.autograd.record():
        if isinstance(loss, (tuple, list)):
            ls = [(l * self._scaler.loss_scale) for l in loss]
        else:
            ls = loss * self._scaler.loss_scale
    mx.autograd.backward(ls)