def dbRestore(self, db_value, context=None):
    if db_value is None:
        return None
    elif isinstance(db_value, (str, unicode)):
        return self.valueFromString(db_value, context=context)
    else:
        return super(AbstractDatetimeColumn, self).dbRestore(db_value,
            context=context)