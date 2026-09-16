def add_chart(self, chart_type, x, y, cx, cy, chart_data):
    rId = self.part.add_chart_part(chart_type, chart_data)
    graphicFrame = self._add_chart_graphicFrame(rId, x, y, cx, cy)
    self._recalculate_extents()
    return self._shape_factory(graphicFrame)