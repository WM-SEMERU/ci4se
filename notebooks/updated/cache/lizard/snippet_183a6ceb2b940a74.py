def has_item(self, hash_key, range_key=None, consistent_read=False):
    try:
        self.get_item(hash_key, range_key=range_key, attributes_to_get=[
            hash_key], consistent_read=consistent_read)
    except dynamodb_exceptions.DynamoDBKeyNotFoundError:
        return False
    return True