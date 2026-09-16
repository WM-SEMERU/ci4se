def format_to_example(table, tabspace=2, indent=2):
    from io import StringIO
    output = StringIO()
    caption, rows = table
    output.write('{0}Examples: {1}\n'.format(' ' * indent * tabspace, caption))
    cols = zip(*rows)
    col_lengths = []
    for col in cols:
        max_length = max([len(format_item(row)) for row in col])
        col_lengths.append(max_length)
    for r, row in enumerate(rows):
        output.write(' ' * (indent + 1) * tabspace)
        output.write('|')
        for c in range(len(col_lengths)):
            output.write(' ')
            output.write(format_item(row[c], r))
            output.write(' ' * (col_lengths[c] - len(format_item(row[c], r))))
            output.write(' |')
        output.write('\n')
    example = output.getvalue()
    output.close()
    return example