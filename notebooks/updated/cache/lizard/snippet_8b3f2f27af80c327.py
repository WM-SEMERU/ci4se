def _flush_tile_queue(self, surface):
    tw, th = self.data.tile_size
    ltw = self._tile_view.left * tw
    tth = self._tile_view.top * th
    surface_blit = surface.blit
    self.data.prepare_tiles(self._tile_view)
    for x, y, l, image in self._tile_queue:
        surface_blit(image, (x * tw - ltw, y * th - tth))