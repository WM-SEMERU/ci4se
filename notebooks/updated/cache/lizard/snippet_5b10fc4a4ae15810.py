def import_laid_out_tensor(mesh, laid_out_tensor, shape, name=None):
    return ImportLaidOutTensorOperation(mesh, laid_out_tensor,
        convert_to_shape(shape), name=name).outputs[0]