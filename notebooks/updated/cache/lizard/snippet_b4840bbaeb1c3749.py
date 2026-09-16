def process_view(self, request, view_func, view_args, view_kwargs):
    view_keys = list(VIEW_METHOD_DATA.keys())
    for key in view_keys:
        del VIEW_METHOD_DATA[key]
    self.view_data = {}
    try:
        cbv = view_func.view_class
    except AttributeError:
        cbv = False
    if cbv:
        self.view_data['cbv'] = True
        klass = view_func.view_class
        self.view_data['bases'] = [base.__name__ for base in inspect.getmro
            (klass)]
        for member in inspect.getmembers(view_func.view_class):
            if member[0] in VIEW_METHOD_WHITEIST and member[0
                ] not in PATCHED_METHODS[klass]:
                decorate_method(klass, member[0])
                PATCHED_METHODS[klass].append(member[0])