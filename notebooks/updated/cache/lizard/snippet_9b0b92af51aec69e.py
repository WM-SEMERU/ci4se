def rename(self, *args, **kwargs):
    axes = validate_axis_style_args(self, args, kwargs, 'mapper', 'rename')
    kwargs.update(axes)
    kwargs.pop('axis', None)
    kwargs.pop('mapper', None)
    return super().rename(**kwargs)