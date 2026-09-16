def upper_band(data, period, env_percentage):
    cb = center_band(data, period)
    ub = [(val * (1 + float(env_percentage))) for val in cb]
    return ub