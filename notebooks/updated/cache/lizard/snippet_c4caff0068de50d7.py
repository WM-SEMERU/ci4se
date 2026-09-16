def data_groups(self, groups, entity_count):
    data = []
    for xid in groups.keys():
        assoc_group_data = self.data_group_association(xid)
        data += assoc_group_data
        entity_count += len(assoc_group_data)
        if entity_count >= self._batch_max_chunk:
            break
    return data, entity_count