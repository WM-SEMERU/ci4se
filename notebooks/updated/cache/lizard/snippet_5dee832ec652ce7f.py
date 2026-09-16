def get_events(self, from_=None, to=None):
    if from_ and (from_ not in self.keys or from_ not in self.events):
        raise EventStore.EventKeyDoesNotExistError(
            'Could not find the from_ key: {0}'.format(from_))
    if to and (to not in self.keys or to not in self.events):
        raise EventStore.EventKeyDoesNotExistError(
            'Could not find the from_ key: {0}'.format(to))
    fromindex = self.keys.index(from_) + 1 if from_ else 0
    toindex = self.keys.index(to) + 1 if to else len(self.events)
    if fromindex > toindex:
        msg = (
            "'From' index came after 'To'. Keys: ({0}, {1}) Indices: ({2}, {3})"
            .format(from_, to, fromindex, toindex))
        raise EventOrderError(msg)
    return ((key, self.events[key]) for key in self.keys[fromindex:toindex])