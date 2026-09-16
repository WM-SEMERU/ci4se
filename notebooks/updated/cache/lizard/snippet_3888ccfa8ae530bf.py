def getProfile(self):
    if self._create:
        return ObjectProfile()
    else:
        if self._profile is None:
            r = self.api.getObjectProfile(self.pid)
            self._profile = parse_xml_object(ObjectProfile, r.content, r.url)
        return self._profile