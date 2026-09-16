def get_mac_address_table(self):
    mac_address_table = []
    switch_style = self.device.facts.get('switch_style', '')
    if switch_style == 'VLAN_L2NG':
        mac_table = junos_views.junos_mac_address_table_switch_l2ng(self.device
            )
    elif switch_style == 'BRIDGE_DOMAIN':
        mac_table = junos_views.junos_mac_address_table(self.device)
    else:
        mac_table = junos_views.junos_mac_address_table_switch(self.device)
    try:
        mac_table.get()
    except RpcError as e:
        if 'l2-learning subsystem' in e.message:
            return []
        else:
            raise
    mac_table_items = mac_table.items()
    default_values = {'mac': '', 'interface': '', 'vlan': 0, 'static':
        False, 'active': True, 'moves': 0, 'last_move': 0.0}
    for mac_table_entry in mac_table_items:
        mac_entry = default_values.copy()
        mac_entry.update({elem[0]: elem[1] for elem in mac_table_entry[1]})
        mac = mac_entry.get('mac')
        if mac == '*':
            continue
        mac_entry['mac'] = napalm.base.helpers.mac(mac)
        mac_address_table.append(mac_entry)
    return mac_address_table