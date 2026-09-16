def _maybe_handle_help(self):
    if self._options.help_request:
        help_printer = HelpPrinter(self._options)
        result = help_printer.print_help()
        self._exiter(result)