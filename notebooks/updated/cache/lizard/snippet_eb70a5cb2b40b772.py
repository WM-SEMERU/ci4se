def copy(self, selection, getter=None, delete=False):
    if getter is None:
        getter = self._get_code
    tab = self.grid.current_table
    selection_bbox = selection.get_bbox()
    if not selection_bbox:
        bb_top, bb_left = self.grid.actions.cursor[:2]
        bb_bottom, bb_right = bb_top, bb_left
    else:
        replace_none = self.main_window.grid.actions._replace_bbox_none
        (bb_top, bb_left), (bb_bottom, bb_right) = replace_none(selection.
            get_bbox())
    data = []
    for __row in xrange(bb_top, bb_bottom + 1):
        data.append([])
        for __col in xrange(bb_left, bb_right + 1):
            if (__row, __col) in selection or not selection_bbox:
                content = getter((__row, __col, tab))
                if delete:
                    try:
                        self.grid.code_array.pop((__row, __col, tab))
                    except KeyError:
                        pass
                if content is None:
                    data[-1].append('')
                else:
                    data[-1].append(content)
            else:
                data[-1].append('')
    return '\n'.join('\t'.join(line) for line in data)