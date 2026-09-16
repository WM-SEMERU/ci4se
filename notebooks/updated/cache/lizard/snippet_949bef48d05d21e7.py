def group_and_sort_leaves_by_ott_id(self):
    ott_id_to_sortable_list = defaultdict(list)
    for node_id in self._edge_by_target.keys():
        node_obj = self._node_by_id[node_id]
        if node_id in self._edge_by_source:
            continue
        otu_id = node_obj['@otu']
        otu_obj = self.otus[otu_id]
        ott_id = otu_obj.get('^ot:ottId')
        is_exemplar = node_obj.get('^ot:isTaxonExemplar', False)
        int_is_exemplar = 0
        if is_exemplar:
            int_is_exemplar = -1
        sortable_el = int_is_exemplar, node_id, node_obj, otu_obj
        ott_id_to_sortable_list[ott_id].append(sortable_el)
    for v in ott_id_to_sortable_list.values():
        v.sort()
    return ott_id_to_sortable_list