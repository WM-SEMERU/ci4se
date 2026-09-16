def getRemoteObject(self, busName, objectPath, interfaces=None,
    replaceKnownInterfaces=False):
    weak_id = busName, objectPath, interfaces
    need_introspection = False
    required_interfaces = set()
    if interfaces is not None:
        ifl = []
        if not isinstance(interfaces, list):
            interfaces = [interfaces]
        for i in interfaces:
            if isinstance(i, interface.DBusInterface):
                ifl.append(i)
                required_interfaces.add(i.name)
            else:
                required_interfaces.add(i)
                if i in interface.DBusInterface.knownInterfaces:
                    ifl.append(interface.DBusInterface.knownInterfaces[i])
                else:
                    need_introspection = True
        if not need_introspection:
            return defer.succeed(RemoteDBusObject(self, busName, objectPath,
                ifl))
    d = self.conn.introspectRemoteObject(busName, objectPath,
        replaceKnownInterfaces)

    def ok(ifaces):
        missing = required_interfaces - {q.name for q in ifaces}
        if missing:
            raise error.IntrospectionFailed(
                'Introspection failed to find interfaces: ' + ','.join(missing)
                )
        prox = RemoteDBusObject(self, busName, objectPath, ifaces)
        self._weakProxies[weak_id] = prox
        return prox
    d.addCallback(ok)
    return d