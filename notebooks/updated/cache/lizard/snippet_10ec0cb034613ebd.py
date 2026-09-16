def get_maps_stats(self):
    tpes = {}
    for m in self.maps:
        if m.tpe in tpes:
            tpes[m.tpe] += 1
        else:
            tpes[m.tpe] = 1
    return tpes