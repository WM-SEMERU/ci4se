def slice_begin(self, tensor_shape, pnum):
    tensor_layout = self.tensor_layout(tensor_shape)
    coordinates = pnum_to_processor_coordinates(self.shape, pnum)
    ret = []
    for dim_size, mesh_axis in zip(tensor_shape.to_integer_list,
        tensor_layout.tensor_axis_to_mesh_axis):
        if mesh_axis is None:
            ret.append(0)
        else:
            ret.append(dim_size // self.shape[mesh_axis].size * coordinates
                [mesh_axis])
    return ret