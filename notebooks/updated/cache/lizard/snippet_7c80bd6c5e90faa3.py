def make_row_dict(row):
    ind = row[row.notnull()].index
    values = row[row.notnull()].values
    return dict(list(zip(ind, values)))