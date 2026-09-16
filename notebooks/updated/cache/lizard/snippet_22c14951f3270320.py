def eval_stats(values, mode):
    if mode == 'raw':
        return values.tolist()
    if mode == 'total':
        mode = 'sum'
    try:
        return getattr(np, mode)(values, axis=0)
    except ValueError:
        pass
    return None