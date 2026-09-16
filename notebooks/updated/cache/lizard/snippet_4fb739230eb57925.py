def enable_alarm_actions(self, alarm_names):
    params = {}
    self.build_list_params(params, alarm_names, 'AlarmNames.member.%s')
    return self.get_status('EnableAlarmActions', params)