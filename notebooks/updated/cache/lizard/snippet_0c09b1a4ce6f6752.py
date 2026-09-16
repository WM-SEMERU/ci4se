def parse_alarm(self, global_params, region, alarm):
    alarm['arn'] = alarm.pop('AlarmArn')
    alarm['name'] = alarm.pop('AlarmName')
    for k in ['AlarmConfigurationUpdatedTimestamp', 'StateReason',
        'StateReasonData', 'StateUpdatedTimestamp']:
        foo = alarm.pop(k) if k in alarm else None
    alarm_id = self.get_non_aws_id(alarm['arn'])
    self.alarms[alarm_id] = alarm