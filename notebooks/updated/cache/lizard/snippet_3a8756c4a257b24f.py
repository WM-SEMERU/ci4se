def create_vlan(self, id_vlan):
    vlan_map = dict()
    vlan_map['vlan_id'] = id_vlan
    code, xml = self.submit({'vlan': vlan_map}, 'PUT', 'vlan/create/')
    return self.response(code, xml)