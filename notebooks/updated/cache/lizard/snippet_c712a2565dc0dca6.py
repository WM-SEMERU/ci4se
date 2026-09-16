def cmd_vehicle(self, args):
    if len(args) < 1:
        print('Usage: vehicle SYSID[:COMPID]')
        return
    a = args[0].split(':')
    self.mpstate.settings.target_system = int(a[0])
    if len(a) > 1:
        self.mpstate.settings.target_component = int(a[1])
    best_link = 0
    best_timestamp = 0
    for i in range(len(self.mpstate.mav_master)):
        m = self.mpstate.mav_master[i]
        m.target_system = self.mpstate.settings.target_system
        m.target_component = self.mpstate.settings.target_component
        if 'HEARTBEAT' in m.messages:
            stamp = m.messages['HEARTBEAT']._timestamp
            src_system = m.messages['HEARTBEAT'].get_srcSystem()
            if stamp > best_timestamp:
                best_link = i
                best_timestamp = stamp
    self.mpstate.settings.link = best_link + 1
    print('Set vehicle %s (link %u)' % (args[0], best_link + 1))