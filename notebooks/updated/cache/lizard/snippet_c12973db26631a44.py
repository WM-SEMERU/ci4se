def _configure_shell(config):
    config.has_section('shell') or config.add_section('shell')
    logger.info(
        """What shells or environments would you like sprinter to work with?
(Sprinter will not try to inject into environments not specified here.)
If you specify 'gui', sprinter will attempt to inject it's state into graphical programs as well.
i.e. environment variables sprinter set will affect programs as well, not just shells
WARNING: injecting into the GUI can be very dangerous. it usually requires a restart
 to modify any environmental configuration."""
        )
    environments = list(enumerate(sorted(SHELL_CONFIG), start=1))
    logger.info('[0]: All, ' + ', '.join([('[%d]: %s' % (index, val)) for 
        index, val in environments]))
    desired_environments = lib.prompt('type the environment, comma-separated',
        default='0')
    for index, val in environments:
        if str(index) in desired_environments or '0' in desired_environments:
            config.set('shell', val, 'true')
        else:
            config.set('shell', val, 'false')