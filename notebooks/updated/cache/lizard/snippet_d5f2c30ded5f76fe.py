def create(cls, name, interface_settings_ref=None, area_id=1, area_type=
    'normal', outbound_filters=None, inbound_filters=None,
    shortcut_capable_area=False, ospfv2_virtual_links_endpoints_container=
    None, ospf_abr_substitute_container=None, comment=None, **kwargs):
    interface_settings_ref = element_resolver(interface_settings_ref
        ) or OSPFInterfaceSetting('Default OSPFv2 Interface Settings').href
    if 'inbound_filters_ref' in kwargs:
        inbound_filters = kwargs.get('inbound_filters_ref')
    if 'outbound_filters_ref' in kwargs:
        outbound_filters = kwargs.get('outbound_filters_ref')
    json = {'name': name, 'area_id': area_id, 'area_type': area_type,
        'comment': comment, 'inbound_filters_ref': element_resolver(
        inbound_filters), 'interface_settings_ref': interface_settings_ref,
        'ospf_abr_substitute_container': ospf_abr_substitute_container,
        'ospfv2_virtual_links_endpoints_container':
        ospfv2_virtual_links_endpoints_container, 'outbound_filters_ref':
        element_resolver(outbound_filters), 'shortcut_capable_area':
        shortcut_capable_area}
    return ElementCreator(cls, json)