def _apply_conv(self, inputs, w):
    w_dw, w_pw = w
    outputs = tf.nn.separable_conv2d(inputs, w_dw, w_pw, rate=self._rate,
        strides=self.stride, padding=self._conv_op_padding, data_format=
        self._data_format)
    return outputs