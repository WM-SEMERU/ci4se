def collect_appendvars(ap_, cls):
    for key, value in cls.__dict__.items():
        if key.startswith('appendvars_'):
            varname = key[11:]
            if varname not in ap_.appendvars:
                ap_.appendvars[varname] = []
            if value not in ap_.appendvars[varname]:
                if not isinstance(value, list):
                    value = [value]
                ap_.appendvars[varname] += value