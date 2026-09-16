def reload_config(self):
    reload_cmd = self.commands.find_by_name('reload-alignak')
    if not reload_cmd:
        logger.error(
            "Cannot restart Alignak : missing command named 'reload-alignak'. Please add one"
            )
        return
    logger.warning('RELOAD command : %s', reload_cmd)
    reload_cmd_line = reload_cmd.command_line
    logger.warning('RELOAD command : %s', reload_cmd_line)
    e_handler = EventHandler({'command': reload_cmd_line, 'timeout': 900})
    e_handler.execute()
    while e_handler.status not in [ACT_STATUS_DONE, ACT_STATUS_TIMEOUT]:
        e_handler.check_finished(64000)
    log_level = 'info'
    if e_handler.status == ACT_STATUS_TIMEOUT or e_handler.exit_status != 0:
        logger.error(
            "Cannot reload Alignak configuration: the 'reload-alignak' command failed with the error code '%d' and the text '%s'."
            , e_handler.exit_status, e_handler.output)
        log_level = 'error'
    self.send_an_element(make_monitoring_log(log_level, 'RELOAD: %s' %
        e_handler.output))