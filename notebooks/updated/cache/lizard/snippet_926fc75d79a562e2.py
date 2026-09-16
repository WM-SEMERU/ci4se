def convert(input_file_name, **kwargs):
    delimiter = kwargs['delimiter'] or ','
    quotechar = kwargs['quotechar'] or '|'
    if six.PY2:
        delimiter = delimiter.encode('utf-8')
        quotechar = quotechar.encode('utf-8')
    with open(input_file_name, 'rb') as input_file:
        reader = csv.reader(input_file, encoding='utf-8', delimiter=
            delimiter, quotechar=quotechar)
        csv_headers = []
        if not kwargs.get('no_header'):
            csv_headers = next(reader)
        csv_rows = [row for row in reader if row]
        if not csv_headers and len(csv_rows) > 0:
            end = len(csv_rows[0]) + 1
            csv_headers = ['Column {}'.format(n) for n in range(1, end)]
    html = render_template(csv_headers, csv_rows, **kwargs)
    return freeze_js(html)