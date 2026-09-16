def data_structure_builder(func):

    @wraps(func)
    def ds_builder_wrapper(function, *args, **kwargs):
        try:
            function = DSBuilder(function)
        except NoBuilder:
            pass
        return func(function, *args, **kwargs)
    return ds_builder_wrapper