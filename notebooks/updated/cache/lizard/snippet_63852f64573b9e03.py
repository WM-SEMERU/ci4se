def custom_grad(self, op, *grads):
    return op_handlers[op.type](self, op, *grads)