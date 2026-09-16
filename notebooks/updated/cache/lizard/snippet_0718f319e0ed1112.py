def _define_helper(flag_name, default_value, docstring, flagtype, required):
    option_name = flag_name if required else '--%s' % flag_name
    get_context_parser().add_argument(option_name, default=default_value,
        help=docstring, type=flagtype)