def order_columns_in_row(fields, unordered_row):
    fields_idx = {f: pos for pos, f in enumerate(fields)}
    return OrderedDict(sorted(unordered_row.items(), key=lambda i:
        fields_idx[i[0]]))