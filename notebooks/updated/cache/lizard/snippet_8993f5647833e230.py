def load_texture(self, file_path, cell_size=(256, 256)):
    super(SpriteSheet, self).load_texture(file_path)
    self.__cell_bounds = cell_size
    self.__generate_cells()