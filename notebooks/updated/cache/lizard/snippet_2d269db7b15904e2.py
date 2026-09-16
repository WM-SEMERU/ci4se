def get_mirror(self):
    mirror = False
    if self.get_diplomacy()['1v1']:
        civs = set()
        for data in self.get_players():
            civs.add(data['civilization'])
        mirror = len(civs) == 1
    return mirror