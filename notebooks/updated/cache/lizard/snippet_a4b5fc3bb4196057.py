def select_balanced_subset(items, select_count, categories,
    select_count_values=None, seed=None):
    rand = random.Random()
    rand.seed(seed)
    if select_count_values is None:
        select_count_values = {item_id: (1) for item_id in items.keys()}
    if sum(select_count_values.values()) < select_count:
        return list(items.keys())
    available_item_ids = sorted(list(items.keys()))
    weight_per_category = np.zeros(len(categories))
    selected_item_ids = []
    available_item_weights = []
    current_select_count = 0
    rand.shuffle(available_item_ids)
    for item_id in available_item_ids:
        weights = items[item_id]
        all_weights = np.zeros(len(categories))
        for category, weight in weights.items():
            all_weights[categories.index(category)] = float(weight)
        available_item_weights.append(all_weights)
    while current_select_count < select_count:
        best_item_index = 0
        best_item_id = None
        best_item_dist = float('inf')
        current_item_index = 0
        while current_item_index < len(available_item_ids
            ) and best_item_dist > 0:
            item_id = available_item_ids[current_item_index]
            item_weights = available_item_weights[current_item_index]
            temp_total_weights = weight_per_category + item_weights
            dist = temp_total_weights.var()
            if dist < best_item_dist:
                best_item_index = current_item_index
                best_item_dist = dist
                best_item_id = item_id
            current_item_index += 1
        weight_per_category += available_item_weights[best_item_index]
        selected_item_ids.append(best_item_id)
        del available_item_ids[best_item_index]
        del available_item_weights[best_item_index]
        current_select_count += select_count_values[best_item_id]
    return selected_item_ids