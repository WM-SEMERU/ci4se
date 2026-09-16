def smart_init_mapping(candidate_mapping, instance1, instance2):
    random.seed()
    matched_dict = {}
    result = []
    no_word_match = []
    for i, candidates in enumerate(candidate_mapping):
        if not candidates:
            result.append(-1)
            continue
        value1 = instance1[i][2]
        for node_index in candidates:
            value2 = instance2[node_index][2]
            if value1 == value2:
                if node_index not in matched_dict:
                    result.append(node_index)
                    matched_dict[node_index] = 1
                    break
        if len(result) == i:
            no_word_match.append(i)
            result.append(-1)
    for i in no_word_match:
        candidates = list(candidate_mapping[i])
        while candidates:
            rid = random.randint(0, len(candidates) - 1)
            candidate = candidates[rid]
            if candidate in matched_dict:
                candidates.pop(rid)
            else:
                matched_dict[candidate] = 1
                result[i] = candidate
                break
    return result