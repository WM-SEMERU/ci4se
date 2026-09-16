def command(state, args):
    args = parser.parse_args(args[1:])
    if args.complete:
        query.files.delete_regexp_complete(state.db)
    elif args.aid is None:
        parser.print_help()
    else:
        aid = state.results.parse_aid(args.aid, default_key='db')
        query.files.delete_regexp(state.db, aid)