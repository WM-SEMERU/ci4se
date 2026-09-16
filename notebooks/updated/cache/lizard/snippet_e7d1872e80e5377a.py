def _format_help(self, scope_info):
    scope = scope_info.scope
    description = scope_info.description
    show_recursive = self._help_request.advanced
    show_advanced = self._help_request.advanced
    color = sys.stdout.isatty()
    help_formatter = HelpFormatter(scope, show_recursive, show_advanced, color)
    return '\n'.join(help_formatter.format_options(scope, description, self
        ._options.get_parser(scope).option_registrations_iter()))