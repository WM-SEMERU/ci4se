def approve_assignment(self, assignment_id):
    try:
        return self._is_ok(self.mturk.approve_assignment(AssignmentId=
            assignment_id))
    except ClientError as ex:
        assignment = self.get_assignment(assignment_id)
        raise MTurkServiceException('Failed to approve assignment {}, {}: {}'
            .format(assignment_id, str(assignment), str(ex)))