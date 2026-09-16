def dry_run(self):
    if self.database_current_migration is None:
        self.printer('~> Woulda initialized: %s\n' % self.name_for_printing())
        return 'inited'
    migrations_to_run = self.migrations_to_run()
    if migrations_to_run:
        self.printer('~> Woulda updated %s:\n' % self.name_for_printing())
        for migration_number, migration_func in migrations_to_run():
            self.printer('   + Would update %s, "%s"\n' % (migration_number,
                migration_func.func_name))
        return 'migrated'