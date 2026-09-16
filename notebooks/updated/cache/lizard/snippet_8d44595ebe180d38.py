def nacm_rule_list_cmdrule_comment(self, **kwargs):
    config = ET.Element('config')
    nacm = ET.SubElement(config, 'nacm', xmlns=
        'urn:ietf:params:xml:ns:yang:ietf-netconf-acm')
    rule_list = ET.SubElement(nacm, 'rule-list')
    name_key = ET.SubElement(rule_list, 'name')
    name_key.text = kwargs.pop('name')
    cmdrule = ET.SubElement(rule_list, 'cmdrule', xmlns=
        'http://tail-f.com/yang/acm')
    name_key = ET.SubElement(cmdrule, 'name')
    name_key.text = kwargs.pop('name')
    comment = ET.SubElement(cmdrule, 'comment')
    comment.text = kwargs.pop('comment')
    callback = kwargs.pop('callback', self._callback)
    return callback(config)