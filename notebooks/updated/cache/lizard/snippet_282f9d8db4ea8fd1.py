def insert(self, table, records, create_cols=False, dtypes=None):
    if self._check_db() is False:
        return
    try:
        table = self.db[table]
    except Exception as e:
        self.err(e, 'Can not find table ' + table)
    t = type(records)
    if t == dict:
        func = table.insert
    elif t == list:
        func = table.insert_many
    else:
        msg = 'Rows datatype ' + str(t
            ) + ' not valid: use a list or a dictionary'
        self.err(msg)
    if create_cols is True:
        try:
            func(records, ensure=True, types=dtypes)
        except Exception as e:
            self.err(e, 'Can not insert create columns and insert data')
        return
    else:
        try:
            func(records, types=dtypes)
        except Exception as e:
            self.err(e, 'Can not insert data')
        return
    self.ok('Rows inserted in the database')