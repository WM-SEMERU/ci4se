def apply_acl(self, equipments, vlan, environment, network):
    vlan_map = dict()
    vlan_map['equipments'] = equipments
    vlan_map['vlan'] = vlan
    vlan_map['environment'] = environment
    vlan_map['network'] = network
    url = 'vlan/apply/acl/'
    code, xml = self.submit({'vlan': vlan_map}, 'POST', url)
    return self.response(code, xml)