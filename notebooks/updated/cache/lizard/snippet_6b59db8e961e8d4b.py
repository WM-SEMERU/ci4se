def get_cube(self, name):
    return Cube(self.get_engine(), name, self.get_cube_model(name))