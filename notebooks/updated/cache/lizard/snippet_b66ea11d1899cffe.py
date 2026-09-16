def get_controller(self):
    command = ovs_vsctl.VSCtlCommand('get-controller', [self.br_name])
    self.run_command([command])
    result = command.result
    return result[0] if len(result) == 1 else result