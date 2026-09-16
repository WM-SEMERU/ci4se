def create_networks(self, ids, id_vlan):
    network_map = dict()
    network_map['ids'] = ids
    network_map['id_vlan'] = id_vlan
    code, xml = self.submit({'network': network_map}, 'PUT', 'network/create/')
    return self.response(code, xml)