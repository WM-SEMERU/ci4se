def update(self):
    url = self.baseurl + '/_status?format=xml'
    response = self.s.get(url)
    response.raise_for_status()
    from xml.etree.ElementTree import XML
    root = XML(response.text)
    for serv_el in root.iter('service'):
        serv = Monit.Service(self, serv_el)
        self[serv.name] = serv
        if self[serv.name].pendingaction:
            time.sleep(1)
            return Monit.update(self)
        if self[serv.name].monitorState == 2:
            time.sleep(1)
            return Monit.update(self)