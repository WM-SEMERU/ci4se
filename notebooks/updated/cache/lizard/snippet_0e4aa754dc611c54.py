def enhance(self):
    self.update({'os_default_templates': SubDict(self.api, self.objName,
        self.payloadObj, self.key, SubItemOsDefaultTemplate)})
    self.update({'operatingsystems': SubDict(self.api, self.objName, self.
        payloadObj, self.key, SubItemOperatingSystem)})