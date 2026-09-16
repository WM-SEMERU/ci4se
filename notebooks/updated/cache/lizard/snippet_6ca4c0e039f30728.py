def _create_archive_table(self, table_name):
    if table_name in self._get_table_names():
        raise KeyError('Table "{}" already exists'.format(table_name))
    try:
        table = self._resource.create_table(TableName=table_name, KeySchema
            =[{'AttributeName': '_id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': '_id', 'AttributeType':
            'S'}], ProvisionedThroughput={'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123})
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
    except ValueError:
        msg = 'Table creation failed'
        assert table_name in self._get_table_names(), msg