def box_type_1(self, X, Y, name, ident, box_width, box_height):
    boxW2 = box_width / 2
    boxH2 = box_height / 2
    x0, y0 = X - boxW2, Y - boxH2
    x1, y1 = X + boxW2, Y + boxH2
    width = x1 - x0
    height = y1 - y0
    box = gui.SvgRectangle(x0, y0, width, height)
    box.set_stroke(width=2, color='black')
    box.set_fill(color='yellow')
    box_name = gui.SvgText(X, Y, name)
    box_name.attributes['text-anchor'] = 'middle'
    box_id = gui.SvgText(X, Y + 15, str(ident))
    box_id.attributes['text-anchor'] = 'middle'
    self.sheet.append([box, box_name, box_id])
    mid_north = [X, Y - boxH2]
    mid_south = [X, Y + boxH2]
    mid_east = [X + boxW2, Y]
    mid_west = [X - boxW2, Y]
    return mid_north, mid_south, mid_east, mid_west