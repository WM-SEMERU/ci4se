def follow_path(self, path, weight=None):
    if len(path) < 2:
        raise ValueError('Paths need at least 2 nodes')
    eng = self.character.engine
    turn_now, tick_now = eng.time
    with eng.plan():
        prevplace = path.pop(0)
        if prevplace != self['location']:
            raise ValueError('Path does not start at my present location')
        subpath = [prevplace]
        for place in path:
            if (prevplace not in self.character.portal or place not in self
                .character.portal[prevplace]):
                raise TravelException("Couldn't follow portal from {} to {}"
                    .format(prevplace, place), path=subpath, traveller=self)
            subpath.append(place)
            prevplace = place
        turns_total = 0
        prevsubplace = subpath.pop(0)
        subsubpath = [prevsubplace]
        for subplace in subpath:
            portal = self.character.portal[prevsubplace][subplace]
            turn_inc = portal.get(weight, 1)
            eng.turn += turn_inc
            self.location = subplace
            turns_total += turn_inc
            subsubpath.append(subplace)
            prevsubplace = subplace
        self.location = subplace
        eng.time = turn_now, tick_now
    return turns_total