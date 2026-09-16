def mavlink_packet(self, m):
    if not self.have_home and m.get_type(
        ) == 'GPS_RAW_INT' and m.fix_type >= 3:
        gen_settings.home_lat = m.lat * 1e-07
        gen_settings.home_lon = m.lon * 1e-07
        self.have_home = True
        if self.pending_start:
            self.start()
    if m.get_type() != 'ATTITUDE':
        return
    t = self.get_time()
    dt = t - self.last_t
    if dt < 0 or dt > 10:
        self.last_t = t
        return
    if dt > 10 or dt < 0.9:
        return
    self.last_t = t
    for a in self.aircraft:
        if not gen_settings.stop:
            a.update(1.0)
            self.pkt_queue.append(a.pickled())
            while len(self.pkt_queue) > len(self.aircraft) * 2:
                self.pkt_queue.pop(0)
    if self.module('map') is not None and not self.menu_added_map:
        self.menu_added_map = True
        self.module('map').add_menu(self.menu)