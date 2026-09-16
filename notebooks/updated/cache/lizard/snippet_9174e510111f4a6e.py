def _load(self, event):
    if not event.data:
        return
    context = self.context()
    schema = self.schema()
    dbname = schema.dbname()
    clean = {}
    for col, value in event.data.items():
        try:
            model_dbname, col_name = col.split('.')
        except ValueError:
            col_name = col
            model_dbname = dbname
        try:
            column = schema.column(col_name)
        except orb.errors.ColumnNotFound:
            column = None
        if model_dbname != dbname or column in clean and isinstance(clean[
            column], Model):
            continue
        elif not column:
            self.__preload[col_name] = value
        else:
            value = column.dbRestore(value, context=context)
            clean[column] = value
    with WriteLocker(self.__dataLock):
        for col, val in clean.items():
            default = val if not isinstance(val, dict) else val.copy()
            self.__values[col.name()] = default, val
            self.__loaded.add(col)
    if self.processEvent(event):
        self.onLoad(event)