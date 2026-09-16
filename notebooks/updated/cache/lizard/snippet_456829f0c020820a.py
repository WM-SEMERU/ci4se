def AddWiFiDevice(self, device_name, iface_name, state):
    path = '/org/freedesktop/NetworkManager/Devices/' + device_name
    self.AddObject(path, WIRELESS_DEVICE_IFACE, {'HwAddress': dbus.String(
        '11:22:33:44:55:66'), 'PermHwAddress': dbus.String(
        '11:22:33:44:55:66'), 'Bitrate': dbus.UInt32(5400), 'Mode': dbus.
        UInt32(2), 'WirelessCapabilities': dbus.UInt32(255), 'AccessPoints':
        dbus.Array([], signature='o')}, [('GetAccessPoints', '', 'ao',
        'ret = self.access_points'), ('GetAllAccessPoints', '', 'ao',
        'ret = self.access_points'), ('RequestScan', 'a{sv}', '', '')])
    dev_obj = dbusmock.get_object(path)
    dev_obj.access_points = []
    dev_obj.AddProperties(DEVICE_IFACE, {'ActiveConnection': dbus.
        ObjectPath('/'), 'AvailableConnections': dbus.Array([], signature=
        'o'), 'AutoConnect': False, 'Managed': True, 'Driver': 'dbusmock',
        'DeviceType': dbus.UInt32(2), 'State': dbus.UInt32(state),
        'Interface': iface_name, 'IpInterface': iface_name})
    self.object_manager_emit_added(path)
    NM = dbusmock.get_object(MANAGER_OBJ)
    devices = NM.Get(MANAGER_IFACE, 'Devices')
    devices.append(path)
    NM.Set(MANAGER_IFACE, 'Devices', devices)
    NM.EmitSignal('org.freedesktop.NetworkManager', 'DeviceAdded', 'o', [path])
    return path