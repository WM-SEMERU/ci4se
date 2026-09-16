def execute(self, statement, params=()):
    con = self.__con or self.connection
    cur = self.__cur or con.cursor()
    if isinstance(statement, list) == False:
        statement = [statement]
        params = [params]
    for state, param in zip(statement, params):
        logger.debug('%s %s' % (state, param))
        cur.execute(state, param)
    if not self.__con:
        con.commit()
        cur.close()
        self.register_modification()