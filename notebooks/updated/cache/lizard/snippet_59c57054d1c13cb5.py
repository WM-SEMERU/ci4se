def plot_data(input_data, xlabel=None, ylabel=None, sed=True, figure=None,
    e_unit=None, ulim_opts={}, errorbar_opts={}):
    import matplotlib.pyplot as plt
    try:
        data = validate_data_table(input_data)
    except TypeError as exc:
        if hasattr(input_data, 'data'):
            data = input_data.data
        elif isinstance(input_data, dict) and 'energy' in input_data.keys():
            data = input_data
        else:
            log.warning(
                'input_data format unknown, no plotting data! Data loading exception: {}'
                .format(exc))
            raise
    if figure is None:
        f = plt.figure()
    else:
        f = figure
    if len(f.axes) > 0:
        ax1 = f.axes[0]
    else:
        ax1 = f.add_subplot(111)
    try:
        old_e_unit = u.Unit(ax1.get_xlabel().split('[')[-1].split(']')[0])
    except ValueError:
        old_e_unit = u.Unit('')
    if e_unit is None and old_e_unit.physical_type == 'energy':
        e_unit = old_e_unit
    elif e_unit is None:
        e_unit = data['energy'].unit
    _plot_data_to_ax(data, ax1, e_unit=e_unit, sed=sed, ylabel=ylabel,
        ulim_opts=ulim_opts, errorbar_opts=errorbar_opts)
    if xlabel is not None:
        ax1.set_xlabel(xlabel)
    elif xlabel is None and ax1.get_xlabel() == '':
        ax1.set_xlabel('$\\mathrm{Energy}$' + ' [{0}]'.format(e_unit.
            to_string('latex_inline')))
    ax1.autoscale()
    return f