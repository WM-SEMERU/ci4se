def applied_scroll_offsets(self):
    if self.displayed_lines[0] == 0:
        top = 0
    else:
        y = self.input_line_to_visible_line[self.ui_content.cursor_position.y]
        top = min(y, self.configured_scroll_offsets.top)
    return ScrollOffsets(top=top, bottom=min(self.ui_content.line_count -
        self.displayed_lines[-1] - 1, self.configured_scroll_offsets.bottom
        ), left=0, right=0)