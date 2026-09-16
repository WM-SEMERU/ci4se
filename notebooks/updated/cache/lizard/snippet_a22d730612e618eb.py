def add_chassis(self, chassis):
    self.chassis_list[chassis] = XenaSocket(self.logger, chassis.ip,
        chassis.port)
    self.chassis_list[chassis].connect()
    KeepAliveThread(self.chassis_list[chassis]).start()
    self.send_command(chassis, 'c_logon', '"{}"'.format(chassis.password))
    self.send_command(chassis, 'c_owner', '"{}"'.format(chassis.owner))