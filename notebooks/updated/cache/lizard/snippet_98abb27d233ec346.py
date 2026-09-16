def add_places(self, places, ret=False):
    if type(places) != list:
        places = [places]
    self.places += places
    if ret:
        return self