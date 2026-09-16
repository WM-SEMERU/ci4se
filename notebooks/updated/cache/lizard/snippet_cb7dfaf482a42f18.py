def create_routine_wrapper_generator(self, rdbms):
    if rdbms == 'mysql':
        module = locate('pystratum_mysql.MySqlRoutineWrapperGenerator')
        return module.MySqlRoutineWrapperGenerator(self.output)
    if rdbms == 'mssql':
        module = locate('pystratum_mssql.MsSqlRoutineWrapperGenerator')
        return module.MsSqlRoutineWrapperGenerator(self.output)
    if rdbms == 'pgsql':
        module = locate('pystratum_pgsql.PgSqlRoutineWrapperGenerator')
        return module.PgSqlRoutineWrapperGenerator(self.output)
    raise Exception("Unknown RDBMS '{0!s}'.".format(rdbms))