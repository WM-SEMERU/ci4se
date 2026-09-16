def get_repository_ids_by_composition(self, composition_id):
    mgr = self._get_provider_manager('REPOSITORY', local=True)
    lookup_session = mgr.get_composition_lookup_session(proxy=self._proxy)
    lookup_session.use_federated_repository_view()
    lookup_session.use_unsequestered_composition_view()
    composition = lookup_session.get_composition(composition_id)
    id_list = []
    if 'assignedRepositoryIds' in composition._my_map:
        for idstr in composition._my_map['assignedRepositoryIds']:
            id_list.append(Id(idstr))
    return IdList(id_list)