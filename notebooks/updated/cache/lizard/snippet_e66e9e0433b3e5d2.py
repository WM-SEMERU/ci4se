def write_conf(self, config_file_type, opener, skip_keys=None):
    blocked_keys = self.keys_blocked_from_output
    if skip_keys:
        blocked_keys.extend(skip_keys)
    if blocked_keys:
        option_defs = self.option_definitions.safe_copy()
        for a_blocked_key in blocked_keys:
            try:
                del option_defs[a_blocked_key]
            except (AttributeError, KeyError):
                pass
        all_keys = [k for k in option_defs.keys_breadth_first(include_dicts
            =True)]
        for key in all_keys:
            candidate = option_defs[key]
            if isinstance(candidate, Namespace) and not len(candidate):
                del option_defs[key]
    else:
        option_defs = self.option_definitions
    if not self.option_definitions.admin.expose_secrets.default:
        for a_key in option_defs.keys_breadth_first():
            an_option = option_defs[a_key]
            if not a_key.startswith('admin') and isinstance(an_option, Option
                ) and an_option.secret:
                option_defs[a_key].value = '*' * 16
                option_defs[a_key].from_string_converter = str
    dispatch_request_to_write(config_file_type, option_defs, opener)