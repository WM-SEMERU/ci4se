def torque_on(self):
    data = []
    data.append(10)
    data.append(self.servoid)
    data.append(RAM_WRITE_REQ)
    data.append(TORQUE_CONTROL_RAM)
    data.append(1)
    data.append(96)
    send_data(data)