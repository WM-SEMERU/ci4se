def get_scans(self):
    code, data = self.send_request('/scans/', method='GET')
    if code != 200:
        msg = 'Failed to retrieve scans. Unexpected code %s'
        raise APIException(msg % code)
    scans = data.get('items', None)
    if scans is None:
        raise APIException('Failed to retrieve scans, no "items" in JSON.')
    scan_instances = []
    for scan_json in scans:
        scan_id = scan_json['id']
        scan_status = scan_json['status']
        scan = Scan(self, scan_id=scan_id, status=scan_status)
        scan_instances.append(scan)
    return scan_instances