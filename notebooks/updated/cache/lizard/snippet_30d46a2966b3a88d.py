def import_from_html(filename_or_fobj, encoding='utf-8', index=0,
    ignore_colspan=True, preserve_html=False, properties=False, table_tag=
    'table', row_tag='tr', column_tag='td|th', *args, **kwargs):
    source = Source.from_file(filename_or_fobj, plugin_name='html', mode=
        'rb', encoding=encoding)
    html = source.fobj.read().decode(source.encoding)
    html_tree = document_fromstring(html)
    tables = html_tree.xpath('//{}'.format(table_tag))
    table = tables[index]
    strip_tags(table, 'thead')
    strip_tags(table, 'tbody')
    row_elements = table.xpath(row_tag)
    table_rows = [_get_row(row, column_tag=column_tag, preserve_html=
        preserve_html, properties=properties) for row in row_elements]
    if properties:
        table_rows[0][-1] = 'properties'
    if preserve_html and kwargs.get('fields', None) is None:
        table_rows[0] = list(map(_extract_node_text, row_elements[0]))
    if ignore_colspan:
        max_columns = max(map(len, table_rows))
        table_rows = [row for row in table_rows if len(row) == max_columns]
    meta = {'imported_from': 'html', 'source': source}
    return create_table(table_rows, *args, meta=meta, **kwargs)