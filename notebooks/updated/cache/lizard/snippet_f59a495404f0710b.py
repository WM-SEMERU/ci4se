def make_fpfList(options):
    user_values = options.fpf
    defaults = ['0.0001', '0.001', '0.01', '0.05']
    if user_values:
        for fpf in user_values:
            if fpf not in defaults:
                defaults.append(fpf)
        defaults.sort()
    return defaults