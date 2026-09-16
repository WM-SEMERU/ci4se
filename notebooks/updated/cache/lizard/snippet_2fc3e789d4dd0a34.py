def disconnect(self):
    logger.info('disconnecting snap7 client')
    result = self.library.Cli_Disconnect(self.pointer)
    check_error(result, context='client')
    return result