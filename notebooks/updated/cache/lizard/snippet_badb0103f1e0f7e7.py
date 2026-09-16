def cli(env, sortby, datacenter, number, name, limit):
    mgr = SoftLayer.NetworkManager(env.client)
    table = formatting.Table(COLUMNS)
    table.sortby = sortby
    vlans = mgr.list_vlans(datacenter=datacenter, vlan_number=number, name=
        name, limit=limit)
    for vlan in vlans:
        table.add_row([vlan['id'], vlan['vlanNumber'], vlan.get('name') or
            formatting.blank(), 'Yes' if vlan['firewallInterfaces'] else
            'No', utils.lookup(vlan, 'primaryRouter', 'datacenter', 'name'),
            vlan['hardwareCount'], vlan['virtualGuestCount'], vlan[
            'totalPrimaryIpAddressCount']])
    env.fout(table)