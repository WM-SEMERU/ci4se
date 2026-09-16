def dispatch_op(self, op_name, args_dict):
    self.logger.debug('Requested `%s` command with `%s` args.' % (op_name,
        args_dict))
    method = getattr(self, 'op_%s' % op_name, None)
    if method is None:
        error_str = '`%s` command is not supported.' % op_name
        self.logger.error(error_str)
        raise DjangoDevException(error_str)
    method(**args_dict)
    self.logger.info('Done.')