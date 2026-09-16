def align_add(tree, key, item, align_thres=2.0):
    for near_key, near_list in get_near_items(tree, key):
        if abs(key - near_key) < align_thres:
            near_list.append(item)
            return
    tree[key] = [item]