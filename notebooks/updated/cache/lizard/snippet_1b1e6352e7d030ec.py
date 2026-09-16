def event_types(self):
    try:
        events = self.rater.find('events')
    except AttributeError:
        raise IndexError('You need to have at least one rater')
    return [x.get('type') for x in events]