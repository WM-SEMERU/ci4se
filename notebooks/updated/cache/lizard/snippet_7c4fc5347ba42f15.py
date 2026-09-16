def _register_and_parse_flags_with_usage(argv=None, flags_parser=
    parse_flags_with_usage):
    if _register_and_parse_flags_with_usage.done:
        raise SystemError('Flag registration can be done only once.')
    define_help_flags()
    original_argv = sys.argv if argv is None else argv
    args_to_main = flags_parser(original_argv)
    if not FLAGS.is_parsed():
        raise Error('FLAGS must be parsed after flags_parser is called.')
    if FLAGS.only_check_args:
        sys.exit(0)
    if FLAGS['verbosity'].using_default_value:
        FLAGS.verbosity = 0
    _register_and_parse_flags_with_usage.done = True
    return args_to_main