def apply_migration(self, migration, **kwargs):
    cprint('\nAttempting to run %s' % migration, 'cyan')
    exists = Migration.select().where(Migration.name == migration).limit(1
        ).first()
    if exists and self.direction == 'up':
        cprint('This migration has already been run on this server', 'red')
        if not self.force or self.fake:
            return False
        else:
            cprint('Force running this migration again', 'yellow')
    module_name = '%s.%s' % (self.module_name, migration)
    try:
        module = importlib.import_module(module_name)
        if not hasattr(module, self.direction):
            raise MigrationException("%s doesn't have %s migration defined" %
                (migration, self.direction))
        getattr(module, self.direction)(self)
        for op in self.operations:
            self.execute_operation(op)
        if not self.fake:
            if self.direction == 'up' and not exists:
                Migration.create(name=migration)
            elif self.direction == 'down' and exists:
                exists.delete_instance()
        cprint('Done', 'green')
    except ImportError:
        raise MigrationException('%s migration not found' % migration)