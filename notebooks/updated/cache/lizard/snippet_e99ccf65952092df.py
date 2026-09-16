def zimbra_to_python(zimbra_dict, key_attribute='n', content_attribute=
    '_content'):
    local_dict = {}
    for item in zimbra_dict:
        local_dict[item[key_attribute]] = item[content_attribute]
    return local_dict