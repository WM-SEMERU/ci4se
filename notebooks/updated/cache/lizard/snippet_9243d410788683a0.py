def enhance(self):
    self.update({'puppetclasses': SubDict(self.api, self.objName, self.
        payloadObj, self.key, SubItemPuppetClasses)})
    self.update({'parameters': SubDict(self.api, self.objName, self.
        payloadObj, self.key, SubItemParameter)})
    self.update({'smart_class_parameters': SubDict(self.api, self.objName,
        self.payloadObj, self.key, ItemSmartClassParameter)})