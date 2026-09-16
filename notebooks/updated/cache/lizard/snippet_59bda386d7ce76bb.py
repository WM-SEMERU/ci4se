def get_console_output(self, instance_id):
    params = {}
    self.build_list_params(params, [instance_id], 'InstanceId')
    return self.get_object('GetConsoleOutput', params, ConsoleOutput, verb=
        'POST')