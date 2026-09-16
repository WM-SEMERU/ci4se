def slicewise(self, fn, *inputs):
    if fn == tf.add:
        assert len(inputs) == 2
        if isinstance(inputs[0], mtf.LazyAllreduceSum):
            return inputs[0] + inputs[1]
    inputs = mtf.convert_args_to_laid_out_tensors(inputs)
    ret = fn(*[(x.one_slice if isinstance(x, self.LaidOutTensor) else x) for
        x in inputs])
    if isinstance(ret, tuple):
        return tuple([self.LaidOutTensor([t]) for t in ret])
    else:
        return self.LaidOutTensor([ret])