def update(self):
    stats = self.get_init_value()
    if self.input_method == 'local':
        glances_processes.update()
        stats = glances_processes.getcount()
    elif self.input_method == 'snmp':
        pass
    self.stats = stats
    return self.stats