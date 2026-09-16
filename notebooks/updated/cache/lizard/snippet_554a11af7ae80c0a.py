def mouse_handler(self, cli, mouse_event):
    b = cli.current_buffer

    def scroll_left():
        b.complete_previous(count=self._rendered_rows, disable_wrap_around=True
            )
        self.scroll = max(0, self.scroll - 1)

    def scroll_right():
        b.complete_next(count=self._rendered_rows, disable_wrap_around=True)
        self.scroll = min(self._total_columns - self._rendered_columns, 
            self.scroll + 1)
    if mouse_event.event_type == MouseEventType.SCROLL_DOWN:
        scroll_right()
    elif mouse_event.event_type == MouseEventType.SCROLL_UP:
        scroll_left()
    elif mouse_event.event_type == MouseEventType.MOUSE_UP:
        x = mouse_event.position.x
        y = mouse_event.position.y
        if x == 0:
            if self._render_left_arrow:
                scroll_left()
        elif x == self._render_width - 1:
            if self._render_right_arrow:
                scroll_right()
        else:
            completion = self._render_pos_to_completion.get((x, y))
            if completion:
                b.apply_completion(completion)