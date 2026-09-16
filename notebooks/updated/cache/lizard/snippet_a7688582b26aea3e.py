def bufsize_validator(kwargs):
    invalid = []
    in_ob = kwargs.get('in', None)
    out_ob = kwargs.get('out', None)
    in_buf = kwargs.get('in_bufsize', None)
    out_buf = kwargs.get('out_bufsize', None)
    in_no_buf = ob_is_tty(in_ob) or ob_is_pipe(in_ob)
    out_no_buf = ob_is_tty(out_ob) or ob_is_pipe(out_ob)
    err = (
        "Can't specify an {target} bufsize if the {target} target is a pipe or TTY"
        )
    if in_no_buf and in_buf is not None:
        invalid.append((('in', 'in_bufsize'), err.format(target='in')))
    if out_no_buf and out_buf is not None:
        invalid.append((('out', 'out_bufsize'), err.format(target='out')))
    return invalid