def exists(self):
    if self.driver == 'sqlite' and not os.path.exists(self.path):
        return False
    self.engine
    try:
        from sqlalchemy.engine.reflection import Inspector
        inspector = Inspector.from_engine(self.engine)
        if 'config' in inspector.get_table_names(schema=self._schema):
            return True
        else:
            return False
    finally:
        self.close_connection()