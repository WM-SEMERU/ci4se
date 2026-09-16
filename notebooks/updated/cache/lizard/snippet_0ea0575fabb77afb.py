def get_learning_objectives(self):
    if not bool(self._my_map['learningObjectiveIds']):
        raise errors.IllegalState('no learningObjectiveIds')
    mgr = self._get_provider_manager('LEARNING')
    if not mgr.supports_objective_lookup():
        raise errors.OperationFailed(
            'Learning does not support Objective lookup')
    lookup_session = mgr.get_objective_lookup_session(proxy=getattr(self,
        '_proxy', None))
    lookup_session.use_federated_objective_bank_view()
    return lookup_session.get_objectives_by_ids(self.
        get_learning_objective_ids())