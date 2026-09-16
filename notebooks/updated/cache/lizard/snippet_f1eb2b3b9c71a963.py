def _lookup_key_parse(table_keys):
    regex_matcher = '\\[([^\\]]+)]'
    valid_dynamodb_datatypes = ['M', 'S', 'N', 'L']
    clean_table_keys = []
    new_keys = []
    for key in table_keys:
        match = re.search(regex_matcher, key)
        if match:
            if match.group(1) in valid_dynamodb_datatypes:
                match_val = str(match.group(1))
                key = key.replace(match.group(0), '')
                new_keys.append({match_val: key})
                clean_table_keys.append(key)
            else:
                raise ValueError(
                    'Stacker does not support looking up the datatype: {}'.
                    format(str(match.group(1))))
        else:
            new_keys.append({'S': key})
            clean_table_keys.append(key)
    key_dict = {}
    key_dict['new_keys'] = new_keys
    key_dict['clean_table_keys'] = clean_table_keys
    return key_dict