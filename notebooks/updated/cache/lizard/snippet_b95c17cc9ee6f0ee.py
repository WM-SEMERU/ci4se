def ConvCnstrMODMask(*args, **kwargs):
    method = kwargs.pop('method', 'fista')
    base = ccmodmsk_class_label_lookup(method)


    class ConvCnstrMODMask(base):

        def __init__(self, *args, **kwargs):
            super(ConvCnstrMODMask, self).__init__(*args, **kwargs)
    _fix_dynamic_class_lookup(ConvCnstrMODMask, method)
    return ConvCnstrMODMask(*args, **kwargs)