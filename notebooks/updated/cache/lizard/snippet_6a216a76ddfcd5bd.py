def entity_copy(args):
    if not args.to_workspace:
        args.to_workspace = args.workspace
    if not args.to_project:
        args.to_project = args.project
    if args.project == args.to_project and args.workspace == args.to_workspace:
        eprint(
            'destination project and namespace must differ from source workspace'
            )
        return 1
    if not args.entities:
        ents = _entity_paginator(args.project, args.workspace, args.
            entity_type, page_size=500, filter_terms=None, sort_direction='asc'
            )
        args.entities = [e['name'] for e in ents]
    prompt = 'Copy {0} {1}(s) from {2}/{3} to {4}/{5}?\n[Y\\n]: '
    prompt = prompt.format(len(args.entities), args.entity_type, args.
        project, args.workspace, args.to_project, args.to_workspace)
    if not args.yes and not _confirm_prompt('', prompt):
        return
    r = fapi.copy_entities(args.project, args.workspace, args.to_project,
        args.to_workspace, args.entity_type, args.entities,
        link_existing_entities=args.link)
    fapi._check_response_code(r, 201)
    return 0