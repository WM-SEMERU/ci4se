def factor_cmap(field_name, palette, factors, start=0, end=None, nan_color=
    'gray'):
    return field(field_name, CategoricalColorMapper(palette=palette,
        factors=factors, start=start, end=end, nan_color=nan_color))