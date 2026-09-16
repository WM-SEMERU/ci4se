def create_user(self, name, password, is_super=False):
    statement = ddl.CreateUser(name=name, password=password, is_super=is_super)
    self._execute(statement)