def virtual_switches(self):
    if not self._virtual_switches:
        self._virtual_switches = VirtualSwitchManager(self)
    return self._virtual_switches