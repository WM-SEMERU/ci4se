def check_hash_key(query_on, key):
    return isinstance(key, BaseCondition
        ) and key.operation == '==' and key.column is query_on.hash_key