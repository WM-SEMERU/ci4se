def extra_args_parser(parser=None, skip_args=None, **kwargs):
    if skip_args is None:
        skip_args = []
    parser, actions = MCMCMetadataIO.extra_args_parser(parser=parser,
        skip_args=skip_args, **kwargs)
    if 'temps' not in skip_args:
        act = parser.add_argument('--temps', nargs='+', default=0, action=
            ParseTempsArg, help=
            "Get the given temperatures. May provide either a sequence of integers specifying the temperatures to plot, or 'all' for all temperatures. Default is to only plot the coldest (= 0) temperature chain."
            )
        actions.append(act)
    return parser, actions