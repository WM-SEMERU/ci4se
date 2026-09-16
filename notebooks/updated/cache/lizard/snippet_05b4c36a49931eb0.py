def filter_macro(func, *args, **kwargs):
    filter_partial = partial(func, *args, **kwargs)


    class FilterMacroMeta(FilterMeta):

        @staticmethod
        def __new__(mcs, name, bases, attrs):
            for attr in WRAPPER_ASSIGNMENTS:
                if hasattr(func, attr):
                    attrs[attr] = getattr(func, attr)
            return super(FilterMacroMeta, mcs).__new__(mcs, func.__name__,
                bases, attrs)

        def __call__(cls, *runtime_args, **runtime_kwargs):
            return filter_partial(*runtime_args, **runtime_kwargs)


    class FilterMacro(with_metaclass(FilterMacroMeta, FilterMacroType)):

        def _apply(self, value):
            return self.__class__()._apply(value)
    return FilterMacro