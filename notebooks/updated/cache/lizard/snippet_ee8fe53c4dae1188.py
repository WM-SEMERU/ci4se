def AddObject(self, path, interface, properties, methods):
    if path in objects:
        raise dbus.exceptions.DBusException('object %s already exists' %
            path, name='org.freedesktop.DBus.Mock.NameError')
    obj = DBusMockObject(self.bus_name, path, interface, properties)
    obj.logfile = self.logfile
    obj.object_manager = self.object_manager
    obj.is_logfile_owner = False
    obj.AddMethods(interface, methods)
    objects[path] = obj