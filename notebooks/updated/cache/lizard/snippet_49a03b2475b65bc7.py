def html2rst(html_string, force_headers=False, center_cells=False,
    center_headers=False):
    if os.path.isfile(html_string):
        file = open(html_string, 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()
        html_string = ''.join(lines)
    table_data, spans, use_headers = html2data(html_string)
    if table_data == '':
        return ''
    if force_headers:
        use_headers = True
    return data2rst(table_data, spans, use_headers, center_cells,
        center_headers)