def _set_axis_formatter(self, axis, dim, formatter):
    if isinstance(dim, list):
        dim = dim[0]
    if formatter is not None:
        pass
    elif dim.value_format:
        formatter = dim.value_format
    elif dim.type in dim.type_formatters:
        formatter = dim.type_formatters[dim.type]
    if formatter:
        axis.set_major_formatter(wrap_formatter(formatter))