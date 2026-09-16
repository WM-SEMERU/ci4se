def plot_world(*args, **kwargs):
    interactive = kwargs.pop('interactive', True)
    if interactive:
        plot_world_with_elegans(*args, **kwargs)
    else:
        plot_world_with_matplotlib(*args, **kwargs)