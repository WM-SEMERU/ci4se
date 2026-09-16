def MultiDestroyFlowStates(self, session_ids, request_limit=None):
    subjects = [session_id.Add('state') for session_id in session_ids]
    to_delete = []
    deleted_requests = []
    for subject, values in self.MultiResolvePrefix(subjects, self.
        FLOW_REQUEST_PREFIX, limit=request_limit):
        for _, serialized, _ in values:
            request = rdf_flow_runner.RequestState.FromSerializedString(
                serialized)
            deleted_requests.append(request)
            response_subject = self.GetFlowResponseSubject(request.
                session_id, request.id)
            to_delete.append(response_subject)
        to_delete.append(subject)
    self.DeleteSubjects(to_delete, sync=True)
    return deleted_requests