def set_alarm_range_sets(self, parameter, sets):
    req = mdb_pb2.ChangeParameterRequest()
    req.action = mdb_pb2.ChangeParameterRequest.SET_ALARMS
    for rs in sets:
        if rs.context:
            context_alarm = req.contextAlarm.add()
            context_alarm.context = rs.context
            alarm_info = context_alarm.alarm
        else:
            alarm_info = req.defaultAlarm
        _add_alarms(alarm_info, rs.watch, rs.warning, rs.distress, rs.
            critical, rs.severe, rs.min_violations)
    url = '/mdb/{}/{}/parameters/{}'.format(self._instance, self._processor,
        parameter)
    response = self._client.post_proto(url, data=req.SerializeToString())
    pti = mdb_pb2.ParameterTypeInfo()
    pti.ParseFromString(response.content)
    print(pti)