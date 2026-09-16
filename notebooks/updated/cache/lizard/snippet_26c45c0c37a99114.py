def extract_operations(self, migrations):
    operations = []
    for migration in migrations:
        for operation in migration.operations:
            if isinstance(operation, RunSQL):
                statements = sqlparse.parse(dedent(operation.sql))
                for statement in statements:
                    operation = SqlObjectOperation.parse(statement)
                    if operation:
                        operations.append(operation)
                        if self.verbosity >= 2:
                            self.stdout.write(' > % -100s (%s)' % (
                                operation, migration))
    return operations