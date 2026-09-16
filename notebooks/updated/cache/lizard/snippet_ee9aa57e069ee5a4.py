def DbDeleteClassAttribute(self, argin):
    self._log.debug('In DbDeleteClassAttribute()')
    if len(argin) < 2:
        self.warn_stream(
            'DataBase::db_delete_class_attribute(): insufficient number of arguments '
            )
        th_exc(DB_IncorrectArguments,
            'insufficient number of arguments to delete class attribute',
            'DataBase::DeleteClassAttribute()')
    klass_name, attr_name = argin[:2]
    self.db.delete_class_attribute(klass_name, attr_name)