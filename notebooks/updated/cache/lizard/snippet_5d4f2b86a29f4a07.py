def process_animation_queue(self, tile_view):
    self._update_time()
    try:
        if self._animation_queue[0].next > self._last_time:
            return
    except IndexError:
        return
    new_tiles = list()
    new_tiles_append = new_tiles.append
    tile_layers = tuple(self.visible_tile_layers)
    get_tile_image = self.get_tile_image
    while self._animation_queue[0].next <= self._last_time:
        token = heappop(self._animation_queue)
        next_frame = token.advance(self._last_time)
        heappush(self._animation_queue, token)
        for position in token.positions.copy():
            x, y, l = position
            if tile_view.collidepoint(x, y):
                self._animated_tile[position] = next_frame.image
                for layer in tile_layers:
                    if layer == l:
                        new_tiles_append((x, y, layer, next_frame.image))
                    else:
                        image = get_tile_image(x, y, layer)
                        if image:
                            new_tiles_append((x, y, layer, image))
            else:
                token.positions.remove(position)
    return new_tiles