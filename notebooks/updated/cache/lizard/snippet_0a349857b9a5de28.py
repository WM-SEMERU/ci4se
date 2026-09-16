def has_material(self, new_material):
    for material in self.materials:
        if material.name == new_material.name:
            return True
    return False