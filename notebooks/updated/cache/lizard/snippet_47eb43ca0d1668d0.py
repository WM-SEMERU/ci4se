def attach_volume(self, xml_bytes):
    root = XML(xml_bytes)
    status = root.findtext('status')
    attach_time = root.findtext('attachTime')
    attach_time = datetime.strptime(attach_time[:19], '%Y-%m-%dT%H:%M:%S')
    return {'status': status, 'attach_time': attach_time}