def get_grade_system_query_session(self):
    if not self.supports_grade_system_query():
        raise errors.Unimplemented()
    return sessions.GradeSystemQuerySession(runtime=self._runtime)