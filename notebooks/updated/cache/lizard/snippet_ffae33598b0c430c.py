def new_tbl(cls, rows, cols, width, height, tableStyleId=None):
    if tableStyleId is None:
        tableStyleId = '{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}'
    xml = cls._tbl_tmpl() % tableStyleId
    tbl = parse_xml(xml)
    rowheight = height // rows
    colwidth = width // cols
    for col in range(cols):
        if col == cols - 1:
            colwidth = width - (cols - 1) * colwidth
        tbl.tblGrid.add_gridCol(width=colwidth)
    for row in range(rows):
        if row == rows - 1:
            rowheight = height - (rows - 1) * rowheight
        tr = tbl.add_tr(height=rowheight)
        for col in range(cols):
            tr.add_tc()
    return tbl