def _get_id2parents(id2parents, item_id, item_obj):
    if item_id in id2parents:
        return id2parents[item_id]
    parent_ids = set()
    for parent_obj in item_obj.parents:
        parent_id = parent_obj.item_id
        parent_ids.add(parent_id)
        parent_ids |= _get_id2parents(id2parents, parent_id, parent_obj)
    id2parents[item_id] = parent_ids
    return parent_ids