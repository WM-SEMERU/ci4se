def _get_dict_of_block_index(self, axis, indices, ordered=False):
    all_partitions_and_idx = [self._get_blocks_containing_index(axis, i) for
        i in indices]
    if ordered:
        partitions_dict = []
        last_part = -1
        for part_idx, internal_idx in all_partitions_and_idx:
            if part_idx == last_part:
                partitions_dict[-1][-1].append(internal_idx)
            else:
                partitions_dict.append((part_idx, [internal_idx]))
            last_part = part_idx
    else:
        partitions_dict = {}
        for part_idx, internal_idx in all_partitions_and_idx:
            if part_idx not in partitions_dict:
                partitions_dict[part_idx] = [internal_idx]
            else:
                partitions_dict[part_idx].append(internal_idx)
    return partitions_dict