def do(parser=None, args=None, in_=None, table_function=None):
    in_ = in_ or sys.stdin
    table_function = table_function or losser.table
    parsed_args = parse(parser=parser, args=args)
    if parsed_args.input_data:
        input_data = open(parsed_args.input_data, 'r').read()
    else:
        input_data = in_.read()
    dicts = json.loads(input_data)
    csv_string = table_function(dicts, parsed_args.columns, csv=True,
        pretty=parsed_args.pretty)
    return csv_string