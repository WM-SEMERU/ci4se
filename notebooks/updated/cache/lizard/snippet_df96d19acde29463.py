def __write_json_file(path, values):
    sort_order = ['name', 'switch', 'comment', 'value', 'flags']
    sorted_values = [OrderedDict(sorted(value.items(), key=lambda value:
        sort_order.index(value[0]))) for value in values]
    with open(path, 'w') as f:
        json.dump(sorted_values, f, indent=2, separators=(',', ': '))