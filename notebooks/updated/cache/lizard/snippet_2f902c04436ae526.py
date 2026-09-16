def create_async_dynamodb_table(self, table_name, read_capacity, write_capacity
    ):
    try:
        dynamodb_table = self.dynamodb_client.describe_table(TableName=
            table_name)
        return False, dynamodb_table
    except botocore.exceptions.ClientError:
        dynamodb_table = self.dynamodb_client.create_table(AttributeDefinitions
            =[{'AttributeName': 'id', 'AttributeType': 'S'}], TableName=
            table_name, KeySchema=[{'AttributeName': 'id', 'KeyType':
            'HASH'}], ProvisionedThroughput={'ReadCapacityUnits':
            read_capacity, 'WriteCapacityUnits': write_capacity})
        if dynamodb_table:
            try:
                self._set_async_dynamodb_table_ttl(table_name)
            except botocore.exceptions.ClientError:
                time.sleep(10)
                self._set_async_dynamodb_table_ttl(table_name)
    return True, dynamodb_table