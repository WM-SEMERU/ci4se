def get_merged_rect(self, grid, key, rect):
    row, col, tab = key
    cell_attributes = grid.code_array.cell_attributes
    merge_area = cell_attributes[row, col, tab]['merge_area']
    if merge_area is None:
        return rect
    else:
        top, left, bottom, right = merge_area
        if top == row and left == col:
            ul_rect = grid.CellToRect(row, col)
            br_rect = grid.CellToRect(bottom, right)
            width = br_rect.x - ul_rect.x + br_rect.width
            height = br_rect.y - ul_rect.y + br_rect.height
            rect = wx.Rect(ul_rect.x, ul_rect.y, width, height)
            return rect