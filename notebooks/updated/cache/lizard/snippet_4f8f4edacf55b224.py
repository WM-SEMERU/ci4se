def magick_to_rio(convert_opts):
    ops = []
    bands = None

    def set_band(x):
        global bands
        if x.upper() == 'RGB':
            x = 'RGB'
        bands = x.upper()
    set_band('RGB')

    def append_sig(arg):
        global bands
        args = list(filter(None, re.split('[,x]+', arg)))
        if len(args) == 1:
            args.append(0.5)
        elif len(args) == 2:
            args[1] = float(args[1].replace('%', '')) / 100.0
        ops.append('sigmoidal {} {} {}'.format(bands, *args))

    def append_gamma(arg):
        global bands
        ops.append('gamma {} {}'.format(bands, arg))

    def append_sat(arg):
        args = list(filter(None, re.split('[,x]+', arg)))
        prop = float(args[1]) / 100
        ops.append('saturation {}'.format(prop))
    nextf = None
    for part in convert_opts.strip().split(' '):
        if part == '-channel':
            nextf = set_band
        elif part == '+channel':
            set_band('RGB')
            nextf = None
        elif part == '-sigmoidal-contrast':
            nextf = append_sig
        elif part == '-gamma':
            nextf = append_gamma
        elif part == '-modulate':
            nextf = append_sat
        else:
            if nextf:
                nextf(part)
            nextf = None
    return ' '.join(ops)