def _to_pandas(ob):
    if isinstance(ob, (pd.Series, pd.DataFrame)):
        return ob
    if ob.ndim == 1:
        return pd.Series(ob)
    elif ob.ndim == 2:
        return pd.DataFrame(ob)
    else:
        raise ValueError(
            'cannot convert array of dim > 2 to a pandas structure')