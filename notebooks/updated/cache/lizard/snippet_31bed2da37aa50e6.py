def describe_table(self, table_name):
    if table_name in self._tables:
        return self._tables[table_name]
    status, description = None, {}
    calls = 0
    while status is not ready:
        calls += 1
        try:
            description = self.dynamodb_client.describe_table(TableName=
                table_name)['Table']
        except botocore.exceptions.ClientError as error:
            raise BloopException('Unexpected error while describing table.'
                ) from error
        status = simple_table_status(description)
    logger.debug(
        'describe_table: table "{}" was in ACTIVE state after {} calls'.
        format(table_name, calls))
    try:
        ttl = self.dynamodb_client.describe_time_to_live(TableName=table_name)
    except botocore.exceptions.ClientError as error:
        raise BloopException('Unexpected error while describing ttl.'
            ) from error
    try:
        backups = self.dynamodb_client.describe_continuous_backups(TableName
            =table_name)
    except botocore.exceptions.ClientError as error:
        raise BloopException(
            'Unexpected error while describing continuous backups.') from error
    description['TimeToLiveDescription'] = {'AttributeName': _read_field(
        ttl, None, 'TimeToLiveDescription', 'AttributeName'),
        'TimeToLiveStatus': _read_field(ttl, None, 'TimeToLiveDescription',
        'TimeToLiveStatus')}
    description['ContinuousBackupsDescription'] = {'ContinuousBackupsStatus':
        _read_field(backups, None, 'ContinuousBackupsDescription',
        'ContinuousBackupsStatus')}
    table = self._tables[table_name] = sanitize_table_description(description)
    return table