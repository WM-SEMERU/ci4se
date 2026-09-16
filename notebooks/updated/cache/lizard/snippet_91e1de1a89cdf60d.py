def logging_syslog_server_syslogip(self, **kwargs):
    config = ET.Element('config')
    logging = ET.SubElement(config, 'logging', xmlns=
        'urn:brocade.com:mgmt:brocade-ras')
    syslog_server = ET.SubElement(logging, 'syslog-server')
    use_vrf_key = ET.SubElement(syslog_server, 'use-vrf')
    use_vrf_key.text = kwargs.pop('use_vrf')
    syslogip = ET.SubElement(syslog_server, 'syslogip')
    syslogip.text = kwargs.pop('syslogip')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)