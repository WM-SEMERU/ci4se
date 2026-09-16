def select_layout(self, layout_type):
    assert layout_type in LayoutTypes._ALL
    if len(self.panes) == 1:
        layout_type = LayoutTypes.EVEN_HORIZONTAL
    if layout_type == LayoutTypes.EVEN_HORIZONTAL:
        self.root = HSplit(self.panes)
    elif layout_type == LayoutTypes.EVEN_VERTICAL:
        self.root = VSplit(self.panes)
    elif layout_type == LayoutTypes.MAIN_HORIZONTAL:
        self.root = HSplit([self.active_pane, VSplit([p for p in self.panes if
            p != self.active_pane])])
    elif layout_type == LayoutTypes.MAIN_VERTICAL:
        self.root = VSplit([self.active_pane, HSplit([p for p in self.panes if
            p != self.active_pane])])
    elif layout_type == LayoutTypes.TILED:
        panes = self.panes
        column_count = math.ceil(len(panes) ** 0.5)
        rows = HSplit()
        current_row = VSplit()
        for p in panes:
            current_row.append(p)
            if len(current_row) >= column_count:
                rows.append(current_row)
                current_row = VSplit()
        if current_row:
            rows.append(current_row)
        self.root = rows
    self.previous_selected_layout = layout_type