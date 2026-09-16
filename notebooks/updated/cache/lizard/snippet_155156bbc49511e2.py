def concat(x, y, axis=0):
    if all([isinstance(df, (pd.DataFrame, pd.Series)) for df in [x, y]]):
        return pd.concat([x, y], axis=axis)
    elif axis == 0:
        return np.concatenate([x, y])
    else:
        return np.column_stack([x, y])