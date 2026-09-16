def dict_to_table(dictionary, list_of_keys=None):
    table = Table()
    if len(dictionary) > 0:
        table['name'] = dictionary.keys()
        prototype = dictionary.values()[0]
        column_names = prototype.keys()
        if list_of_keys is not None:
            column_names = filter(lambda key: key in list_of_keys, column_names
                )
        for column_name in column_names:
            table[column_name] = map(lambda x: x[column_name], dictionary.
                values())
    return table