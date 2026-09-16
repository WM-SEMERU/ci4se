def control(self, instances, action):
    if not isinstance(instances, list) and not isinstance(instances, tuple):
        instances = [instances]
    actions = {'start': {'operation': 'StartInstances', 'response_data_key':
        'StartingInstances', 'InstanceIds': instances}, 'stop': {
        'operation': 'StopInstances', 'response_data_key':
        'StoppingInstances', 'InstanceIds': instances}, 'reboot': {
        'operation': 'RebootInstances', 'response_data_key': 'return',
        'InstanceIds': instances}, 'terminate': {'operation':
        'TerminateInstances', 'response_data_key': 'TerminatingInstances',
        'InstanceIds': instances}, 'protect': {'operation':
        'ModifyInstanceAttribute', 'response_data_key': 'return',
        'Attribute': 'disableApiTermination', 'Value': 'true'}, 'unprotect':
        {'operation': 'ModifyInstanceAttribute', 'response_data_key':
        'return', 'Attribute': 'disableApiTermination', 'Value': 'false'}}
    if action in ('protect', 'unprotect'):
        for instance in instances:
            self.call(InstanceId=instance, **actions[action])
        return 'true'
    else:
        return self.call(**actions[action])