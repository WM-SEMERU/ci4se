def kernel_command_line(self, kernel_command_line):
    log.info(
        'QEMU VM "{name}" [{id}] has set the QEMU kernel command line to {kernel_command_line}'
        .format(name=self._name, id=self._id, kernel_command_line=
        kernel_command_line))
    self._kernel_command_line = kernel_command_line