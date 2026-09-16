def add_arguments(self, parser):
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--downgrade', action='store_true', help=
        'downgrade the J-Link firmware')
    group.add_argument('-u', '--upgrade', action='store_true', help=
        'upgrade the J-Link firmware')
    return self.add_common_arguments(parser, False)