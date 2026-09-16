def mutate_if(df, predicate, fun):
    cols = list()
    for col in df:
        try:
            if predicate(df[col]):
                cols.append(col)
        except:
            pass
    df[cols] = df[cols].apply(fun)
    return df