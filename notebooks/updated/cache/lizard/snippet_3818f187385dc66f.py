def make_slices(self, tf_tensor, tensor_shape):
    tensor_layout = self.tensor_layout(tensor_shape)
    slice_shape = self.slice_shape(tensor_shape)

    def my_fn(pnum):
        if tensor_layout.is_fully_replicated:
            return tf_tensor
        else:
            slice_begin = self.slice_begin(tensor_shape, pnum)
            return tf.slice(tf_tensor, slice_begin, slice_shape)
    return parallel([tf_tensor.device] * self.size, my_fn, list(xrange(self
        .size)))