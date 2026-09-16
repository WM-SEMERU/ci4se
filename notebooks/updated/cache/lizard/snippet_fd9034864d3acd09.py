def DbGetClassInheritanceForDevice(self, argin):
    self._log.debug('In DbGetClassInheritanceForDevice()')
    return self.db.get_class_inheritance_for_device(argin)