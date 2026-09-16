def DbPutClassAttributeProperty(self, argin):
    self._log.debug('In DbPutClassAttributeProperty()')
    class_name = argin[0]
    nb_attributes = int(argin[1])
    self.db.put_class_attribute_property(class_name, nb_attributes, argin[2:])