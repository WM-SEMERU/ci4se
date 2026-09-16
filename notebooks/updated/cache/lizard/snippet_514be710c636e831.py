def _copy_margin(self, cli, lazy_screen, new_screen, write_position, move_x,
    width):
    xpos = write_position.xpos + move_x
    ypos = write_position.ypos
    margin_write_position = WritePosition(xpos, ypos, width, write_position
        .height)
    self._copy_body(cli, lazy_screen, new_screen, margin_write_position, 0,
        width)