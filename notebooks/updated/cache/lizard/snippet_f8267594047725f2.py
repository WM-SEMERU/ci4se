def _render_map(self, surface, rect, surfaces):
    self._tile_queue = self.data.process_animation_queue(self._tile_view)
    self._tile_queue and self._flush_tile_queue(self._buffer)
    if not self._anchored_view:
        self._clear_surface(surface, self._previous_blit)
    offset = -self._x_offset + rect.left, -self._y_offset + rect.top
    with surface_clipping_context(surface, rect):
        self._previous_blit = surface.blit(self._buffer, offset)
        if surfaces:
            surfaces_offset = -offset[0], -offset[1]
            self._draw_surfaces(surface, surfaces_offset, surfaces)