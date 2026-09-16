def draw_visual(self, visual, event=None):
    prof = Profiler()
    self.set_current()
    try:
        self._drawing = True
        if visual not in self._draw_order:
            self._draw_order[visual] = self._generate_draw_order()
        order = self._draw_order[visual]
        stack = []
        invisible_node = None
        for node, start in order:
            if start:
                stack.append(node)
                if invisible_node is None:
                    if not node.visible:
                        invisible_node = node
                    elif hasattr(node, 'draw'):
                        node.draw()
                        prof.mark(str(node))
            else:
                if node is invisible_node:
                    invisible_node = None
                stack.pop()
    finally:
        self._drawing = False