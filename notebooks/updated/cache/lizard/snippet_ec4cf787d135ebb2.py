def get_spaced_plot_colors(n, start=45, saturation_adjustment=0.7,
    saturation=0.65, lightness=1.0, prefix=''):
    assert n > 0
    if n <= 5:
        return ggplot_color_wheel(n, start=start, saturation_adjustment=
            saturation_adjustment, saturation=saturation, lightness=
            lightness, prefix=prefix)
    else:
        plot_colors = ggplot_color_wheel(n, start=start,
            saturation_adjustment=saturation_adjustment, saturation=
            saturation, lightness=lightness, prefix=prefix)
        hp = dumb_relative_half_prime(n)
        color_wheel = [plot_colors[x % n] for x in range(0, hp * n, hp)]
        if not len(color_wheel) == len(set(color_wheel)):
            raise Exception(
                'The color wheel was not generated correctly. Are {0} and {1} relatively prime?'
                .format(n, hp))
        return color_wheel