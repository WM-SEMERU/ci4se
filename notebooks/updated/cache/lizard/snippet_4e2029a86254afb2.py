def do_printActivity(self, args):
    parser = CommandArgumentParser('printActivity')
    parser.add_argument(dest='index', type=int, help='refresh')
    args = vars(parser.parse_args(args))
    index = args['index']
    activity = self.activities[index]
    pprint(activity)