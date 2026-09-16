def update(self, muted=values.unset, hold=values.unset, hold_url=values.
    unset, hold_method=values.unset, announce_url=values.unset,
    announce_method=values.unset, wait_url=values.unset, wait_method=values
    .unset, beep_on_exit=values.unset, end_conference_on_exit=values.unset,
    coaching=values.unset, call_sid_to_coach=values.unset):
    data = values.of({'Muted': muted, 'Hold': hold, 'HoldUrl': hold_url,
        'HoldMethod': hold_method, 'AnnounceUrl': announce_url,
        'AnnounceMethod': announce_method, 'WaitUrl': wait_url,
        'WaitMethod': wait_method, 'BeepOnExit': beep_on_exit,
        'EndConferenceOnExit': end_conference_on_exit, 'Coaching': coaching,
        'CallSidToCoach': call_sid_to_coach})
    payload = self._version.update('POST', self._uri, data=data)
    return ParticipantInstance(self._version, payload, account_sid=self.
        _solution['account_sid'], conference_sid=self._solution[
        'conference_sid'], call_sid=self._solution['call_sid'])