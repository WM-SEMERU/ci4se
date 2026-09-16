def on_size(self, event):
    state = self.state
    self.need_redraw = True
    if state.report_size_changes:
        size = self.frame.GetSize()
        if size != self.last_size:
            self.last_size = size
            state.out_queue.put(MPImageNewSize(size))