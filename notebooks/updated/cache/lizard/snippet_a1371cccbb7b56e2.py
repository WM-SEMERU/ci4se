def execute(self):
    from ambry.mprlib import execute_sql
    execute_sql(self._bundle.library, self.record_content)