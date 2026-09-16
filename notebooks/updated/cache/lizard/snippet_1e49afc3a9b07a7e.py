def inserir(self, id_grupo_l3, id_ambiente_logico, id_divisao, link,
    id_filter=None, acl_path=None, ipv4_template=None, ipv6_template=None,
    min_num_vlan_1=None, max_num_vlan_1=None, min_num_vlan_2=None,
    max_num_vlan_2=None, vrf=None):
    ambiente_map = dict()
    ambiente_map['id_grupo_l3'] = id_grupo_l3
    ambiente_map['id_ambiente_logico'] = id_ambiente_logico
    ambiente_map['id_divisao'] = id_divisao
    ambiente_map['id_filter'] = id_filter
    ambiente_map['link'] = link
    ambiente_map['acl_path'] = acl_path
    ambiente_map['ipv4_template'] = ipv4_template
    ambiente_map['ipv6_template'] = ipv6_template
    ambiente_map['min_num_vlan_1'] = min_num_vlan_1
    ambiente_map['max_num_vlan_1'] = max_num_vlan_1
    ambiente_map['min_num_vlan_2'] = min_num_vlan_2
    ambiente_map['max_num_vlan_2'] = max_num_vlan_2
    ambiente_map['vrf'] = vrf
    code, xml = self.submit({'ambiente': ambiente_map}, 'POST', 'ambiente/')
    return self.response(code, xml)