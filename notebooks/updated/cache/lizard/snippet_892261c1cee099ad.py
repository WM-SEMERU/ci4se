def print_info(self):
    table = PrettyTable()
    start_string = 'DutSerial {} \n'.format(self.name)
    row = []
    info_string = ''
    if self.config:
        info_string = (info_string +
            'Configuration for this DUT:\n\n {} \n'.format(self.config))
    if self.comport:
        table.add_column('COM port', [])
        row.append(self.comport)
    if self.port:
        if hasattr(self.port, 'baudrate'):
            table.add_column('Baudrate', [])
            row.append(self.port.baudrate)
        if hasattr(self.port, 'xonxoff'):
            table.add_column('XON/XOFF', [])
            row.append(self.port.xonxoff)
        if hasattr(self.port, 'timeout'):
            table.add_column('Timeout', [])
            row.append(self.port.timeout)
        if hasattr(self.port, 'rtscts'):
            table.add_column('RTSCTS', [])
            row.append(self.port.rtscts)
    if self.location:
        table.add_column('Location', [])
        row.append('X = {}, Y = {}'.format(self.location.x_coord, self.
            location.y_coord))
    self.logger.info(start_string)
    self.logger.debug(info_string)
    table.add_row(row)
    print(table)