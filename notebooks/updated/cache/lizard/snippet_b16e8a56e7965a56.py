def update(self):
    existing_frames = self._frames
    self._frames = {}

    def create_layout_from_node(node):
        if isinstance(node, window_arrangement.Window):
            key = node, node.editor_buffer
            frame = existing_frames.get(key)
            if frame is None:
                frame, pt_window = self._create_window_frame(node.editor_buffer
                    )
                node.pt_window = pt_window
            self._frames[key] = frame
            return frame
        elif isinstance(node, window_arrangement.VSplit):
            return VSplit([create_layout_from_node(n) for n in node],
                padding=1, padding_char=self.get_vertical_border_char(),
                padding_style='class:frameborder')
        if isinstance(node, window_arrangement.HSplit):
            return HSplit([create_layout_from_node(n) for n in node])
    layout = create_layout_from_node(self.window_arrangement.active_tab.root)
    self._fc.content = layout