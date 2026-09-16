def toPyModel(model_ptr):
    if bool(model_ptr) == False:
        raise ValueError('Null pointer')
    m = model_ptr.contents
    m.__createfrom__ = 'C'
    return m