def create_column_index(annotations):
    _column_index = OrderedDict({'Column Name': annotations['Column Name']})
    categorical_rows = annotation_rows('C:', annotations)
    _column_index.update(categorical_rows)
    numerical_rows = {name: [(float(x) if x != '' else float('NaN')) for x in
        values] for name, values in annotation_rows('N:', annotations).items()}
    _column_index.update(numerical_rows)
    column_index = pd.MultiIndex.from_tuples(list(zip(*_column_index.values
        ())), names=list(_column_index.keys()))
    if len(column_index.names) == 1:
        name = column_index.names[0]
        column_index = column_index.get_level_values(name)
    return column_index