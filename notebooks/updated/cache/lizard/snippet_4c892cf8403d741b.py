def command(self):
    print('pynYNAB CSV import')
    args = self.parser.parse_args()
    verify_common_args(args)
    verify_csvimport(args.schema, args.accountname)
    client = clientfromkwargs(**args)
    delta = do_csvimport(args, client)
    client.push(expected_delta=delta)