def DbGetClassAttributeList(self, argin):
    self._log.debug('In DbGetClassAttributeList()')
    class_name = argin[0]
    wildcard = replace_wildcard(argin[1])
    return self.db.get_class_attribute_list(class_name, wildcard)