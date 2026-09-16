def send_config_set(self, config_commands=None, exit_config_mode=False,
    delay_factor=1, max_loops=150, strip_prompt=False, strip_command=False,
    config_mode_command=None):
    return super(VyOSSSH, self).send_config_set(config_commands=
        config_commands, exit_config_mode=exit_config_mode, delay_factor=
        delay_factor, max_loops=max_loops, strip_prompt=strip_prompt,
        strip_command=strip_command, config_mode_command=config_mode_command)