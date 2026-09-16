def execute_async(self, command, callback=None):
    try:
        logger.debug('{0}: execute async "{1}"with callback {2}'.format(
            self.target_address, command, callback))
        future = self.executor.submit(self.execute, command)
        if callback is not None:
            future.add_done_callback(callback)
        return future
    except (AuthenticationException, SSHException, ChannelException,
        SocketError) as ex:
        logger.critical('{0} execution failed on {1} with exception:{2}'.
            format(command, self.target_address, ex))
        raise SSHCommandError(self.target_address, command, ex)