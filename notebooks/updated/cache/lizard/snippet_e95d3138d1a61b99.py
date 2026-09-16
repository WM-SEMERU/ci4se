def run(self):

    async def run_command():
        try:
            self.result = self.command(context=self.context, **self.kwargs)
        except Exception as error:
            self.exception = error
            print(error)
            import traceback
            traceback.print_exc()
            import sys
            self.context.response.fail(code='COMMAND_EXECUTION_ERROR',
                message='Failed to execute command due to internal error',
                error=error).console(whitespace=1)
    self._has_started = True
    self._loop = asyncio.new_event_loop()
    self._loop.run_until_complete(run_command())
    self._loop.close()
    self._loop = None
    self.completed_at = datetime.utcnow()