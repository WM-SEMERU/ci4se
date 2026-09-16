def calc_model(cortex, model_argument, model_hemi=Ellipsis, radius=np.pi / 3):
    if pimms.is_str(model_argument):
        h = (cortex.chirality if model_hemi is Ellipsis else None if 
            model_hemi is None else model_hemi)
        model = retinotopy_model(model_argument, hemi=h, radius=radius)
    else:
        model = model_argument
    if not isinstance(model, RegisteredRetinotopyModel):
        raise ValueError('model must be a RegisteredRetinotopyModel')
    return model