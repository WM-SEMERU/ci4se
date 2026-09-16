def all_same_proj(self):
    all_areas = [x.attrs.get('area', None) for x in self.values()]
    all_areas = [x for x in all_areas if x is not None]
    return all(all_areas[0].proj_str == x.proj_str for x in all_areas[1:])