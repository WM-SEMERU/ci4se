def do_output(self, *args):
    if args:
        action, params = args[0], args[1:]
        log.debug('Pass %s directly to output with %s', action, params)
        function = getattr(self.output, 'do_' + action, None)
        if function:
            function(*params)