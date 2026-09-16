def add_json_report_optgroup(parser):
    g = parser.add_argument_group('JSON Report Options')
    g.add_argument('--json-indent', action='store', default=2, type=int)