def load_tile_lowres(self, tile):
    if tile.zoom == self.min_zoom:
        return None
    lat, lon = tile.coord()
    width2 = TILES_WIDTH
    height2 = TILES_HEIGHT
    for zoom2 in range(tile.zoom - 1, self.min_zoom - 1, -1):
        width2 /= 2
        height2 /= 2
        if width2 == 0 or height2 == 0:
            break
        tile_info = self.coord_to_tile(lat, lon, zoom2)
        key = tile_info.key()
        if key in self._tile_cache:
            img = self._tile_cache[key]
            if img == self._unavailable:
                continue
        else:
            path = self.tile_to_path(tile_info)
            try:
                img = cv.LoadImage(path)
                self._tile_cache[key] = img
                while len(self._tile_cache) > self.cache_size:
                    self._tile_cache.popitem(0)
            except IOError as e:
                continue
        availx = min(TILES_WIDTH - tile_info.offsetx, width2)
        availy = min(TILES_HEIGHT - tile_info.offsety, height2)
        if availx != width2 or availy != height2:
            continue
        cv.SetImageROI(img, (tile_info.offsetx, tile_info.offsety, width2,
            height2))
        img2 = cv.CreateImage((width2, height2), 8, 3)
        try:
            cv.Copy(img, img2)
        except Exception:
            continue
        cv.ResetImageROI(img)
        scaled = cv.CreateImage((TILES_WIDTH, TILES_HEIGHT), 8, 3)
        cv.Resize(img2, scaled)
        return scaled
    return None