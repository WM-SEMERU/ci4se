def template_runner(client, parser, args):
    if args.builtin_list:
        aomi.template.builtin_list()
    elif args.builtin_info:
        aomi.template.builtin_info(args.builtin_info)
    elif args.template and args.destination and args.vault_paths:
        aomi.render.template(client, args.template, args.destination, args.
            vault_paths, args)
    else:
        parser.print_usage()
        sys.exit(2)
    sys.exit(0)