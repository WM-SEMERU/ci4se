def format_optional_vector(x):
    if x is None or np.all(np.isnan(x)):
        return 'none'
    else:
        return format_vector(x)