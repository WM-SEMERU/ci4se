def flatten_tree_to_ident_hashes(item_or_tree, lucent_id=TRANSLUCENT_BINDER_ID
    ):
    if 'contents' in item_or_tree:
        tree = item_or_tree
        if tree['id'] != lucent_id:
            yield tree['id']
        for i in tree['contents']:
            for x in flatten_tree_to_ident_hashes(i, lucent_id):
                yield x
    else:
        item = item_or_tree
        yield item['id']