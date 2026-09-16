def _add_comparison_methods(cls):
    cls.__eq__ = _make_comparison_op(operator.eq, cls)
    cls.__ne__ = _make_comparison_op(operator.ne, cls)
    cls.__lt__ = _make_comparison_op(operator.lt, cls)
    cls.__gt__ = _make_comparison_op(operator.gt, cls)
    cls.__le__ = _make_comparison_op(operator.le, cls)
    cls.__ge__ = _make_comparison_op(operator.ge, cls)