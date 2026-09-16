def GetPlaylists(self, start, max_count, order, reversed):
    cv = convert2dbus
    return self.iface.GetPlaylists(cv(start, 'u'), cv(max_count, 'u'), cv(
        order, 's'), cv(reversed, 'b'))