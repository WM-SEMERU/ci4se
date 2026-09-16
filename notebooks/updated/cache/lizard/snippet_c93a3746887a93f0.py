def database_current_migration(self):
    if not self.migration_table.exists(self.session.bind):
        return None
    if self.migration_data is None:
        return None
    return self.migration_data.version