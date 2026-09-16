def mavlink_packet(self, msg):
    for i in range(len(self.graphs) - 1, -1, -1):
        if not self.graphs[i].is_alive():
            self.graphs[i].close()
            self.graphs.pop(i)
    for g in self.graphs:
        g.add_mavlink_packet(msg)