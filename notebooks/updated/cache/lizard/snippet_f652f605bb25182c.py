def add_jardiff_optgroup(parser):
    og = parser.add_argument_group('JAR Checking Options')
    og.add_argument('--ignore-jar-entry', action='append', default=[])
    og.add_argument('--ignore-jar-signature', action='store_true', default=
        False, help='Ignore JAR signing changes')
    og.add_argument('--ignore-manifest', action='store_true', default=False,
        help='Ignore changes to manifests')
    og.add_argument('--ignore-manifest-subsections', action='store_true',
        default=False, help='Ignore changes to manifest subsections')
    og.add_argument('--ignore-manifest-key', action='append', default=[],
        help='case-insensitive manifest keys to ignore')