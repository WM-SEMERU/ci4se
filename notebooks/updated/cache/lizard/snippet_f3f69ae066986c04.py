def _check_dhcp_server(self, vboxnet):
    properties = yield from self._execute('list', ['dhcpservers'])
    flag_dhcp_server_found = False
    for prop in properties.splitlines():
        try:
            name, value = prop.split(':', 1)
        except ValueError:
            continue
        if name.strip() == 'NetworkName' and value.strip().endswith(vboxnet):
            flag_dhcp_server_found = True
        if flag_dhcp_server_found and name.strip() == 'Enabled':
            if value.strip() == 'Yes':
                return True
    return False