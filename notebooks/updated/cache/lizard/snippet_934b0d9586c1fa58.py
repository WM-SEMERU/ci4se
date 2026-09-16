def delete_tc(self):
    rule_finder = TcShapingRuleFinder(logger=logger, tc=self)
    filter_param = rule_finder.find_filter_param()
    if not filter_param:
        message = 'shaping rule not found ({}).'.format(rule_finder.
            get_filter_string())
        if rule_finder.is_empty_filter_condition():
            message += (
                ' you can delete all of the shaping rules with --all option.')
        logger.error(message)
        return 1
    logger.info('delete a shaping rule: {}'.format(dict(filter_param)))
    filter_del_command = (
        '{command:s} del dev {dev:s} protocol {protocol:s} parent {parent:} handle {handle:s} prio {prio:} u32'
        .format(command=get_tc_base_command(TcSubCommand.FILTER), dev=
        rule_finder.get_parsed_device(), protocol=filter_param.get(Tc.Param
        .PROTOCOL), parent='{:s}:'.format(rule_finder.find_parent().split(
        ':')[0]), handle=filter_param.get(Tc.Param.FILTER_ID), prio=
        filter_param.get(Tc.Param.PRIORITY)))
    result = run_command_helper(command=filter_del_command,
        ignore_error_msg_regexp=None, notice_msg=None)
    rule_finder.clear()
    if not rule_finder.is_any_filter():
        logger.debug('there are no filters remain. delete qdiscs.')
        self.delete_all_tc()
    return result