def pixels_to_tiles(self, coords, clamp=True):
    tile_coords = Vector2()
    tile_coords.X = int(coords[0]) / self.spritesheet[0].width
    tile_coords.Y = int(coords[1]) / self.spritesheet[0].height
    if clamp:
        tile_coords.X, tile_coords.Y = self.clamp_within_range(tile_coords.
            X, tile_coords.Y)
    return tile_coords