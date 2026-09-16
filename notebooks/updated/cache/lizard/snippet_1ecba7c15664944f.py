def get_stars_of_children_of(self, component):
    stars = self.get_stars()
    orbits = self.get_orbits()
    stars_children = []
    for child in self.get_children_of(component):
        if child in stars:
            stars_children.append(child)
        elif child in orbits:
            stars_children += self.get_stars_of_children_of(child)
        else:
            pass
    return stars_children