def plot_expected_repeat_purchases(model, title=
    'Expected Number of Repeat Purchases per Customer', xlabel=
    'Time Since First Purchase', ax=None, label=None, **kwargs):
    from matplotlib import pyplot as plt
    if ax is None:
        ax = plt.subplot(111)
    if plt.matplotlib.__version__ >= '1.5':
        color_cycle = ax._get_lines.prop_cycler
        color = coalesce(kwargs.pop('c', None), kwargs.pop('color', None),
            next(color_cycle)['color'])
    else:
        color_cycle = ax._get_lines.color_cycle
        color = coalesce(kwargs.pop('c', None), kwargs.pop('color', None),
            next(color_cycle))
    max_T = model.data['T'].max()
    times = np.linspace(0, max_T, 100)
    ax.plot(times, model.expected_number_of_purchases_up_to_time(times),
        color=color, label=label, **kwargs)
    times = np.linspace(max_T, 1.5 * max_T, 100)
    ax.plot(times, model.expected_number_of_purchases_up_to_time(times),
        color=color, ls='--', **kwargs)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.legend(loc='lower right')
    return ax