def get_all_events(self):
    self.all_events = {}
    events = self.tree.findall('EVENT')
    events += self.tree.findall('CC')
    for e in events:
        event_id = e.attrib['id']
        if event_id in self._static_events:
            continue
        event_type = e.find('type').text
        try:
            self.all_events[event_type].append(event_id)
        except KeyError:
            self.all_events[event_type] = [event_id]