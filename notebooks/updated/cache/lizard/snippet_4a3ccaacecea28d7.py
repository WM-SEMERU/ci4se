def flat_model(tree):
    names = []
    for columns in viewvalues(tree):
        for col in columns:
            if isinstance(col, dict):
                col_name = list(col)[0]
                names += [(col_name + '__' + c) for c in flat_model(col)]
            else:
                names.append(col)
    return names