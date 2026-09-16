def create_view(operations, operation):
    operations.execute('CREATE VIEW %s AS %s' % (operation.target.name,
        operation.target.sqltext))