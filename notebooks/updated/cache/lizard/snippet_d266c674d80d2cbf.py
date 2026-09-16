def expand_output_files(value, *args, **kwargs):
    if any(isinstance(x, dynamic) for x in args) or any(isinstance(y,
        dynamic) for y in kwargs.values()):
        return sos_targets(_undetermined=value)
    else:
        return sos_targets(*args, **kwargs, _undetermined=False, _source=
            env.sos_dict['step_name'])