def sortedby(item_list, key_list, reverse=False):
    assert len(item_list) == len(key_list
        ), 'Expected same len. Got: %r != %r' % (len(item_list), len(key_list))
    sorted_list = [item for key, item in sorted(list(zip(key_list,
        item_list)), reverse=reverse)]
    return sorted_list