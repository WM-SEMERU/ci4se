def _expand_interface_name(self, interface_brief):
    if self.interface_map.get(interface_brief):
        return self.interface_map.get(interface_brief)
    command = 'show int {}'.format(interface_brief)
    output = self._send_command(command)
    first_line = output.splitlines()[0]
    if 'line protocol' in first_line:
        full_int_name = first_line.split()[0]
        self.interface_map[interface_brief] = full_int_name
        return self.interface_map.get(interface_brief)
    else:
        return interface_brief