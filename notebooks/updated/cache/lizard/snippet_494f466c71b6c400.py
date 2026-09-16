def list_attached_team(context, id, sort, limit, where, verbose):
    result = topic.list_teams(context, id=id, sort=sort, limit=limit, where
        =where)
    utils.format_output(result, context.format, verbose=verbose)