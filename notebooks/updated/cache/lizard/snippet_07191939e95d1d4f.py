def sset_loop(args):
    fiss_func = __cmd_to_func(args.action)
    if not fiss_func:
        eprint("invalid FISS cmd '" + args.action + "'")
        return 1
    r = fapi.get_entities(args.project, args.workspace, 'sample_set')
    fapi._check_response_code(r, 200)
    sample_sets = [entity['name'] for entity in r.json()]
    args.entity_type = 'sample_set'
    for sset in sample_sets:
        print('\n# {0}::{1}/{2} {3}'.format(args.project, args.workspace,
            sset, args.action))
        args.entity = sset
        try:
            result = fiss_func(args)
        except Exception as e:
            status = __pretty_print_fc_exception(e)
            if not args.keep_going:
                return status
        printToCLI(result)
    return 0