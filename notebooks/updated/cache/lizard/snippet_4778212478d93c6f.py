def get_autocomplete_options_by_scope(self):
    autocomplete_options_by_scope = defaultdict(set)

    def get_from_parser(parser):
        oschi = HelpInfoExtracter.get_option_scope_help_info_from_parser(parser
            )
        option_help_infos = oschi.basic + oschi.recursive
        for ohi in option_help_infos:
            autocomplete_options_by_scope[oschi.scope].update(ohi.
                unscoped_cmd_line_args)
            autocomplete_options_by_scope[oschi.scope].update(ohi.
                scoped_cmd_line_args)
            if issubclass(ohi.registering_class, TaskBase):
                goal_scope = oschi.scope.partition('.')[0]
                autocomplete_options_by_scope[goal_scope].update(ohi.
                    scoped_cmd_line_args)
    self.context.options.walk_parsers(get_from_parser)
    return autocomplete_options_by_scope