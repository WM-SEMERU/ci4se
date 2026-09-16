def get_items_stats(key, value):
    itemized_key = key.split(':')
    slab_id = itemized_key[1]
    metric = itemized_key[2]
    tags = ['slab:{}'.format(slab_id)]
    return metric, tags, value