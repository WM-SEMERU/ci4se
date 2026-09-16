def r_squared(model, fit_result, data):
    y_is = [data[var] for var in model if var in data]
    x_is = [value for var, value in data.items() if var.name in model.
        __signature__.parameters]
    y_bars = [(np.mean(y_i) if y_i is not None else None) for y_i in y_is]
    f_is = model(*x_is, **fit_result.params)
    SS_res = np.sum([np.sum((y_i - f_i) ** 2) for y_i, f_i in zip(y_is,
        f_is) if y_i is not None])
    SS_tot = np.sum([np.sum((y_i - y_bar) ** 2) for y_i, y_bar in zip(y_is,
        y_bars) if y_i is not None])
    return 1 - SS_res / SS_tot