def get_records(self):
    if self.exhausted:
        return []
    if self.empty_responses >= CALLS_TO_REACH_HEAD:
        return self._apply_get_records_response(self.session.
            get_stream_records(self.iterator_id))
    while self.empty_responses < CALLS_TO_REACH_HEAD and not self.exhausted:
        records = self._apply_get_records_response(self.session.
            get_stream_records(self.iterator_id))
        if records:
            return records
    return []