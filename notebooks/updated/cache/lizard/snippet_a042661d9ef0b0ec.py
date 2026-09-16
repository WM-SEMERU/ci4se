def get_bank_ids_by_assessment_part(self, assessment_part_id):
    mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
    lookup_session = mgr.get_assessment_part_lookup_session(proxy=self._proxy)
    lookup_session.use_federated_bank_view()
    assessment_part = lookup_session.get_assessment_part(assessment_part_id)
    id_list = []
    for idstr in assessment_part._my_map['assignedBankIds']:
        id_list.append(Id(idstr))
    return IdList(id_list)