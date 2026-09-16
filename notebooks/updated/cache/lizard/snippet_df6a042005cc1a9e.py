def slice(self, tf_tensor, tensor_shape):
    tensor_layout = self.tensor_layout(tensor_shape)
    if tensor_layout.is_fully_replicated:
        return self.LaidOutTensor([tf_tensor])
    else:
        slice_shape = self.slice_shape(tensor_shape)
        slice_begins = [self.slice_begin(tensor_shape, pnum) for pnum in
            xrange(self.size)]
        slice_begins_tensor = tf.stack(slice_begins)
        selected_slice_begin = tf.gather(slice_begins_tensor, self.pnum_tensor)
        return self.LaidOutTensor([tf.slice(tf_tensor, selected_slice_begin,
            slice_shape)])