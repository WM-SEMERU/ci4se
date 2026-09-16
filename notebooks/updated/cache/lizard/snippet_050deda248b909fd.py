def create_table(self, table_name, model):
    table = create_table_request(table_name, model)
    try:
        self.dynamodb_client.create_table(**table)
        is_creating = True
    except botocore.exceptions.ClientError as error:
        handle_table_exists(error, model)
        is_creating = False
    return is_creating