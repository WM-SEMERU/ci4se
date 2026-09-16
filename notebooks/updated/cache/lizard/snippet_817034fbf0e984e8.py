def _get_dvs_uplink_portgroup(dvs, portgroup_name):
    for portgroup in dvs.portgroup:
        if portgroup.name == portgroup_name:
            return portgroup
    return None