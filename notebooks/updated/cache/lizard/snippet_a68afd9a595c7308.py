def set_default_alarm_ranges(self, parameter, watch=None, warning=None,
    distress=None, critical=None, severe=None, min_violations=1):
    req = mdb_pb2.ChangeParameterRequest()
    req.action = mdb_pb2.ChangeParameterRequest.SET_DEFAULT_ALARMS
    if watch or warning or distress or critical or severe:
        _add_alarms(req.defaultAlarm, watch, warning, distress, critical,
            severe, min_violations)
    url = '/mdb/{}/{}/parameters/{}'.format(self._instance, self._processor,
        parameter)
    response = self._client.post_proto(url, data=req.SerializeToString())