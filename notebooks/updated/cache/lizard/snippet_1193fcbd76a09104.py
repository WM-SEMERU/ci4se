def getRankMaps(self):
    rankMaps = []
    for preference in self.preferences:
        rankMaps.append(preference.getRankMap())
    return rankMaps