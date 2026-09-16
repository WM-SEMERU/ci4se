def fmt_val(val, shorten=True):
    val = repr(val)
    max = 50
    if shorten:
        if len(val) > max:
            close = val[-1]
            val = val[0:max - 4] + '...'
            if close in ('>', "'", '"', ']', '}', ')'):
                val = val + close
    return val