def conv2d(self, x_in: Connection, w_in: Connection, receptive_field_size,
    filters_number, stride=1, padding=1, name=''):
    x_cols = self.tensor_3d_to_cols(x_in, receptive_field_size, stride=
        stride, padding=padding)
    mul = self.transpose(self.matrix_multiply(x_cols, w_in), 0, 2, 1)
    output = self.reshape(mul, (-1, filters_number, receptive_field_size,
        receptive_field_size))
    output.name = name
    return output