def log_run(self):
    version = get_system_spec()['raiden']
    cursor = self.conn.cursor()
    cursor.execute('INSERT INTO runs(raiden_version) VALUES (?)', [version])
    self.maybe_commit()