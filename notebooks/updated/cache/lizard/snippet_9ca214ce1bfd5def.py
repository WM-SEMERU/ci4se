def make_node(self, x):
    x = theano.tensor.as_tensor_variable(x)
    if isinstance(self.operator, Functional):
        out_type = theano.tensor.TensorVariable(theano.tensor.TensorType(
            self.operator.domain.dtype, ()))
    else:
        out_type = theano.tensor.TensorVariable(theano.tensor.TensorType(
            self.operator.range.dtype, [False] * len(self.operator.range.
            shape)))
    return theano.Apply(self, [x], [out_type.type()])