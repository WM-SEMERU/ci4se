def load(self, filename):
    f = open(filename, mode='r')
    version_line = f.readline().strip()
    if version_line == 'QGC WPL 100':
        readfn = self._read_waypoints_v100
    elif version_line == 'QGC WPL 110':
        readfn = self._read_waypoints_v110
    elif version_line == 'QGC WPL PB 110':
        readfn = self._read_waypoints_pb_110
    else:
        f.close()
        raise MAVWPError("Unsupported waypoint format '%s'" % version_line)
    self.clear()
    readfn(f)
    f.close()
    return len(self.wpoints)