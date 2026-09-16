def calc_ethsw_port(self, port_num, port_def):
    port_def = port_def.split(' ')
    if len(port_def) == 4:
        destination = {'device': port_def[2], 'port': port_def[3]}
    else:
        destination = {'device': 'NIO', 'port': port_def[2]}
    port = {'id': self.port_id, 'name': str(port_num), 'port_number': int(
        port_num), 'type': port_def[0], 'vlan': int(port_def[1])}
    self.node['ports'].append(port)
    self.calc_link(self.node['id'], self.port_id, port['name'], destination)
    self.port_id += 1