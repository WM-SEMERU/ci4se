def _parse_arguments():
    parser = get_base_arguments(get_parser())
    parser = get_tc_arguments(parser)
    args, unknown = parser.parse_known_args()
    return args, unknown