def get_my_learning_path_session_for_objective_bank(self, objective_bank_id,
    proxy):
    if not objective_bank_id:
        raise NullArgument
    if not self.supports_my_learning_path():
        raise Unimplemented()
    try:
        from . import sessions
    except ImportError:
        raise OperationFailed()
    proxy = self._convert_proxy(proxy)
    try:
        session = sessions.MyLearningPathSession(objective_bank_id=
            objective_bank_id, proxy=proxy, runtime=self._runtime)
    except AttributeError:
        raise OperationFailed()
    return session