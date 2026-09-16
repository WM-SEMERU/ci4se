def render_arrow(self, label, start, end, direction, i):
    level = self.levels.index(end - start) + 1
    x_start = self.offset_x + start * self.distance + self.arrow_spacing
    if self.direction == 'rtl':
        x_start = self.width - x_start
    y = self.offset_y
    x_end = self.offset_x + (end - start
        ) * self.distance + start * self.distance - self.arrow_spacing * (self
        .highest_level - level) / 4
    if self.direction == 'rtl':
        x_end = self.width - x_end
    y_curve = self.offset_y - level * self.distance / 2
    if self.compact:
        y_curve = self.offset_y - level * self.distance / 6
    if y_curve == 0 and len(self.levels) > 5:
        y_curve = -self.distance
    arrowhead = self.get_arrowhead(direction, x_start, y, x_end)
    arc = self.get_arc(x_start, y, y_curve, x_end)
    label_side = 'right' if self.direction == 'rtl' else 'left'
    return TPL_DEP_ARCS.format(id=self.id, i=i, stroke=self.arrow_stroke,
        head=arrowhead, label=label, label_side=label_side, arc=arc)