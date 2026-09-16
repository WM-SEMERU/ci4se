def _set_motion_detection(self, enable):
    url = ('%s/ISAPI/System/Video/inputs/channels/1/motionDetection' % self
        .root_url)
    enabled = self._motion_detection_xml.find(self.element_query('enabled'))
    if enabled is None:
        _LOGGING.error("Couldn't find 'enabled' in the xml")
        _LOGGING.error('XML: %s', ET.tostring(self._motion_detection_xml))
        return
    enabled.text = 'true' if enable else 'false'
    xml = ET.tostring(self._motion_detection_xml)
    try:
        response = self.hik_request.put(url, data=xml, timeout=CONNECT_TIMEOUT)
    except (requests.exceptions.RequestException, requests.exceptions.
        ConnectionError) as err:
        _LOGGING.error('Unable to set MotionDetection, error: %s', err)
        return
    if response.status_code == requests.codes.unauthorized:
        _LOGGING.error('Authentication failed')
        return
    if response.status_code != requests.codes.ok:
        _LOGGING.error('Unable to set motion detection: %s', response.text)
    self.motion_detection = enable