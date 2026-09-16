def SetPosition(self, track_id, position):
    self.iface.SetPosition(convert2dbus(track_id, 'o'), convert2dbus(
        position, 'x'))