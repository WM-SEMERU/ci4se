def netconf_state_datastores_datastore_name(self, **kwargs):
    config = ET.Element('config')
    netconf_state = ET.SubElement(config, 'netconf-state', xmlns=
        'urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring')
    datastores = ET.SubElement(netconf_state, 'datastores')
    datastore = ET.SubElement(datastores, 'datastore')
    name = ET.SubElement(datastore, 'name')
    name.text = kwargs.pop('name')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)