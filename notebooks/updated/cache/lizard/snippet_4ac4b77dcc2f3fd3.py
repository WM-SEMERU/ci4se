def _update_submission(self, submission):
    submission._comments_by_id[self.name] = self
    self._submission = submission
    if self._replies:
        for reply in self._replies:
            reply._update_submission(submission)