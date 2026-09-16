def _max_form(f, colname):
    df = f.stack(level=0)[[colname]].stack().unstack(level=1).reset_index(level
        =1, drop=True)
    return df.idxmax(axis=1)