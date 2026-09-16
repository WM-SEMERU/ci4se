def invoke(self, args, initial_invocation_data=None, out_file=None):
    from .util import CommandResultItem
    if not isinstance(args, (list, tuple)):
        raise TypeError('args should be a list or tuple.')
    exit_code = 0
    try:
        args = self.completion.get_completion_args() or args
        out_file = out_file or self.out_file
        self.logging.configure(args)
        logger.debug('Command arguments: %s', args)
        self.raise_event(EVENT_CLI_PRE_EXECUTE)
        if CLI._should_show_version(args):
            self.show_version()
            self.result = CommandResultItem(None)
        else:
            self.invocation = self.invocation_cls(cli_ctx=self, parser_cls=
                self.parser_cls, commands_loader_cls=self.
                commands_loader_cls, help_cls=self.help_cls, initial_data=
                initial_invocation_data)
            cmd_result = self.invocation.execute(args)
            self.result = cmd_result
            exit_code = self.result.exit_code
            output_type = self.invocation.data['output']
            if cmd_result and cmd_result.result is not None:
                formatter = self.output.get_formatter(output_type)
                self.output.out(cmd_result, formatter=formatter, out_file=
                    out_file)
        self.raise_event(EVENT_CLI_POST_EXECUTE)
    except KeyboardInterrupt as ex:
        self.result = CommandResultItem(None, error=ex)
        exit_code = 1
    except Exception as ex:
        exit_code = self.exception_handler(ex)
        self.result = CommandResultItem(None, error=ex)
    finally:
        pass
    self.result.exit_code = exit_code
    return exit_code