def all_stars(self):
    stars = []
    for item in self._data:
        if isinstance(item, LinkedEPSFStar):
            stars.extend(item.all_stars)
        else:
            stars.append(item)
    return stars