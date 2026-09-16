def mesh_axis_to_cumprod(self, tensor_shape):
    tensor_layout = self.tensor_layout(tensor_shape)
    ma2ta = tensor_layout.mesh_axis_to_tensor_axis(self.ndims)
    ta2cumprod = tensor_shape.cumprod
    return [(None if ta is None else ta2cumprod[ta]) for ta in ma2ta]