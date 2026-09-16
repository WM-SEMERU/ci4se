def set_output(self, output_names, output_dims):
    spec = self.spec
    nn_spec = self.nn_spec
    for idx, dim in enumerate(output_dims):
        spec.description.output[idx].type.multiArrayType.ClearField('shape')
        spec.description.output[idx].type.multiArrayType.shape.extend(dim)
        spec.description.output[idx
            ].type.multiArrayType.dataType = _Model_pb2.ArrayFeatureType.DOUBLE