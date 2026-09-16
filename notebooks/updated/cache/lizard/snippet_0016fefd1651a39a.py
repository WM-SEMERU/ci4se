def default_jardiff_options(updates=None):
    parser = create_optparser()
    options, _args = parser.parse_args(list())
    if updates:
        options._update_careful(updates)
    return options