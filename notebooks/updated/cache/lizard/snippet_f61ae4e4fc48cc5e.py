def parse_port(port_obj, owner):
    profile = port_obj.get_port_profile()
    props = utils.nvlist_to_dict(profile.properties)
    if props['port.port_type'] == 'DataInPort':
        return DataInPort(port_obj, owner)
    elif props['port.port_type'] == 'DataOutPort':
        return DataOutPort(port_obj, owner)
    elif props['port.port_type'] == 'CorbaPort':
        return CorbaPort(port_obj, owner)
    else:
        return Port(port_obj, owner)