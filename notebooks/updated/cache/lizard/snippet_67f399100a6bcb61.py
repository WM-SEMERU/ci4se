def draw_rect(self, rect):
    check_int_err(lib.SDL_RenderDrawRect(self._ptr, rect._ptr))