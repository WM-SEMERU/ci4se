def mux(index, *mux_ins, **kwargs):
    if kwargs:
        if len(kwargs) != 1 or 'default' not in kwargs:
            try:
                result = select(index, **kwargs)
                import warnings
                warnings.warn(
                    'Predicates are being deprecated in Mux. Use the select operator instead.'
                    , stacklevel=2)
                return result
            except Exception:
                bad_args = [k for k in kwargs.keys() if k != 'default']
                raise PyrtlError('unknown keywords %s applied to mux' % str
                    (bad_args))
        default = kwargs['default']
    else:
        default = None
    short_by = 2 ** len(index) - len(mux_ins)
    if short_by > 0:
        if default is not None:
            mux_ins = list(mux_ins)
            extention = [default] * short_by
            mux_ins.extend(extention)
    if 2 ** len(index) != len(mux_ins):
        raise PyrtlError(
            'Mux select line is %d bits, but selecting from %d inputs. ' %
            (len(index), len(mux_ins)))
    if len(index) == 1:
        return select(index, falsecase=mux_ins[0], truecase=mux_ins[1])
    half = len(mux_ins) // 2
    return select(index[-1], falsecase=mux(index[0:-1], *mux_ins[:half]),
        truecase=mux(index[0:-1], *mux_ins[half:]))