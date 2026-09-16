def get_metadata(model):
    if not isinstance(model, Model):
        raise SynphotError('{0} is not a model.'.format(model))
    if isinstance(model, _CompoundModel):
        metadata = model._tree.evaluate(METADATA_OPERATORS, getter=None)
    else:
        metadata = deepcopy(model.meta)
    return metadata