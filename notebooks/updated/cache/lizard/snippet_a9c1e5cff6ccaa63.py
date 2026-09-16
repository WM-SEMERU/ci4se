def event_matches(self, event, simple=False, keys=False):
    if keys:
        return self._get('event/%s/matches/keys' % event)
    else:
        return [Match(raw) for raw in self._get('event/%s/matches%s' % (
            event, '/simple' if simple else ''))]