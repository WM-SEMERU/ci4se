def find_rows_by_string(tab, names, colnames=['assoc']):
    mask = np.empty(len(tab), dtype=bool)
    mask.fill(False)
    names = [name.lower().replace(' ', '') for name in names]
    for colname in colnames:
        if colname not in tab.columns:
            continue
        col = tab[[colname]].copy()
        col[colname] = defchararray.replace(defchararray.lower(col[colname]
            ).astype(str), ' ', '')
        for name in names:
            mask |= col[colname] == name
    return mask