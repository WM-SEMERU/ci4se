def _fix_channels(self, op, attrs, inputs):
    if op not in [mx.sym.Convolution, mx.sym.Deconvolution, mx.sym.
        FullyConnected]:
        return attrs
    weight_name = self._renames[inputs[1]]
    if not weight_name in self._params:
        raise ValueError('Unable to get channels/units attr from onnx graph.')
    else:
        wshape = self._params[weight_name].shape
        assert len(wshape) >= 2, 'Weights shape is invalid: {}'.format(wshape)
        if op in [mx.sym.FullyConnected]:
            attrs['num_hidden'] = wshape[0]
        elif op == mx.sym.Convolution:
            attrs['num_filter'] = wshape[0]
        elif op == mx.sym.Deconvolution:
            attrs['num_filter'] = wshape[1]
    return attrs