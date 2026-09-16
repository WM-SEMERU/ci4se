def rowcol_from_template(target_tab, template_tab=0):
    for row, tab in S.row_heights.keys():
        if tab == target_tab:
            S.row_heights.pop((row, tab))
        if tab == template_tab:
            S.row_heights[row, target_tab] = S.row_heights[row, tab]
    for col, tab in S.col_widths.keys():
        if tab == target_tab:
            S.col_widths.pop((col, tab))
        if tab == template_tab:
            S.col_widths[col, target_tab] = S.col_widths[col, tab]
    return 'Table {tab} adjusted.'.format(tab=target_tab)