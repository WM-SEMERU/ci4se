def _layout_position(elem):
    row = elem.attrib.get('row')
    column = elem.attrib.get('column')
    alignment = elem.attrib.get('alignment')
    if row is None or column is None:
        if alignment is None:
            return ()
        return 0, _parse_alignment(alignment)
    row = int(row)
    column = int(column)
    rowspan = int(elem.attrib.get('rowspan', 1))
    colspan = int(elem.attrib.get('colspan', 1))
    if alignment is None:
        return row, column, rowspan, colspan
    return row, column, rowspan, colspan, _parse_alignment(alignment)