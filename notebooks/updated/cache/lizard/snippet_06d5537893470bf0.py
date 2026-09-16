def unmerge(self, unmerge_area, tab):
    top, left, bottom, right = unmerge_area
    selection = Selection([(top, left)], [(bottom, right)], [], [], [])
    attr = {'merge_area': None, 'locked': False}
    self._set_cell_attr(selection, tab, attr)