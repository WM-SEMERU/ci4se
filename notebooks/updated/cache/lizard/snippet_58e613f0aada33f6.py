def plot_energy_signature(meter_data, temperature_data, temp_col=None, ax=
    None, title=None, figsize=None, **kwargs):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        raise ImportError('matplotlib is required for plotting.')
    temperature_mean = compute_temperature_features(meter_data.index,
        temperature_data)
    usage_per_day = compute_usage_per_day_feature(meter_data, series_name=
        'meter_value')
    df = merge_features([usage_per_day, temperature_mean.temperature_mean])
    if figsize is None:
        figsize = 10, 4
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    if temp_col is None:
        temp_col = 'temperature_mean'
    ax.scatter(df[temp_col], df.meter_value, **kwargs)
    ax.set_xlabel('Temperature')
    ax.set_ylabel('Energy Use per Day')
    if title is not None:
        ax.set_title(title)
    return ax