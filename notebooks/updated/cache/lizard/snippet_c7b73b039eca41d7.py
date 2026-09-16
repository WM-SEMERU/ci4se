def _mem_update(self, net):
    if net.op != '@':
        raise PyrtlInternalError
    memid = net.op_param[0]
    write_addr = self.value[net.args[0]]
    write_val = self.value[net.args[1]]
    write_enable = self.value[net.args[2]]
    if write_enable:
        self.memvalue[memid][write_addr] = write_val