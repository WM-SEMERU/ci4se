def verify_configs_against_options(self, options):
    error_log = []
    for config in self.config.configs():
        for section in config.sections():
            if section == GLOBAL_SCOPE_CONFIG_SECTION:
                scope = GLOBAL_SCOPE
            else:
                scope = section
            try:
                valid_options_under_scope = set(options.for_scope(scope))
            except Config.ConfigValidationError:
                error_log.append('Invalid scope [{}] in {}'.format(section,
                    config.configpath))
            else:
                all_options_under_scope = set(config.configparser.options(
                    section)) - set(config.configparser.defaults())
                for option in all_options_under_scope:
                    if option not in valid_options_under_scope:
                        error_log.append("Invalid option '{}' under [{}] in {}"
                            .format(option, section, config.configpath))
    if error_log:
        for error in error_log:
            logger.error(error)
        raise Config.ConfigValidationError(
            """Invalid config entries detected. See log for details on which entries to update or remove.
(Specify --no-verify-config to disable this check.)"""
            )