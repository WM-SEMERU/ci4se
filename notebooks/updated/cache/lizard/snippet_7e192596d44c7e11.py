def to_commandline(o):
    if isinstance(o, str) and o.startswith('@{') and o.endswith('}'):
        return o
    else:
        return classes.to_commandline(o)