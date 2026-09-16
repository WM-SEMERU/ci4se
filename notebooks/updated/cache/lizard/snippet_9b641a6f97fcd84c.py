def get_objective_requisite_assignment_session_for_objective_bank(self,
    objective_bank_id, proxy, *args, **kwargs):
    if not objective_bank_id:
        raise NullArgument
    if not self.supports_objective_requisite_assignment():
        raise Unimplemented()
    try:
        from . import sessions
    except ImportError:
        raise OperationFailed()
    proxy = self._convert_proxy(proxy)
    try:
        session = sessions.ObjectiveRequisiteAssignmentSession(
            objective_bank_id=objective_bank_id, proxy=proxy, runtime=self.
            _runtime)
    except AttributeError:
        raise OperationFailed()
    return session