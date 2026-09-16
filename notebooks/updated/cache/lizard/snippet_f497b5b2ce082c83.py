def detach_events(self, *events):
    reg = self.registry
    delete = defaultdict(list)
    all_events = reg.events
    for e in events:
        regexp = getattr(e.regexp, 're', e.regexp)
        iotype = e.iotype
        if e in all_events[iotype].get(regexp, []):
            all_events[iotype][regexp].remove(e)
            if not all_events[iotype][regexp]:
                del all_events[iotype][regexp]
                delete[iotype].append(regexp)
    for iotype, regexps in delete.items():
        reg.events_re[iotype] = [r for r in reg.events_re[iotype] if r[0]
             not in regexps]