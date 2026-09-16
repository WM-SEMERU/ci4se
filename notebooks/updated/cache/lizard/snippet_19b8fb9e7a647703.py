def _get_scale_and_shape(self, parm):
    if self.scale is True:
        if self.shape is True:
            model_shape = parm[-1]
            model_scale = parm[-2]
        else:
            model_shape = 0
            model_scale = parm[-1]
    else:
        model_scale = 0
        model_shape = 0
    if self.skewness is True:
        model_skewness = parm[-3]
    else:
        model_skewness = 0
    return model_scale, model_shape, model_skewness