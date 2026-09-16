def dbname(self, value):
    self._dbname = value
    self._connectionXML.set('dbname', value)