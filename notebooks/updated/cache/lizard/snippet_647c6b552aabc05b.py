def feedback_summaries(self):
    if self._feedback_summaries is None:
        self._feedback_summaries = FeedbackSummaryList(self._version,
            account_sid=self._solution['account_sid'])
    return self._feedback_summaries