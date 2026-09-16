def convert_to_scalars(cls, ops, kwargs):
    from qnet.algebra.core.scalar_algebra import Scalar, ScalarValue
    scalar_ops = []
    for op in ops:
        if not isinstance(op, Scalar):
            scalar_ops.append(ScalarValue(op))
        else:
            scalar_ops.append(op)
    return scalar_ops, kwargs