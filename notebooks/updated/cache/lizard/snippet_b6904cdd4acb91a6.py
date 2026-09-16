def set_fog_density(self, density):
    if density < 0 or density > 1:
        raise HolodeckException('Fog density should be between 0 and 1')
    self._should_write_to_command_buffer = True
    command_to_send = ChangeFogDensityCommand(density)
    self._commands.add_command(command_to_send)