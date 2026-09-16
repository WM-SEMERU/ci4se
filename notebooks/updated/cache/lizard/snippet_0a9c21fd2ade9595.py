def _parse_get_snapshot_schedule(cls, args):
    argparser = ArgumentParser(prog='cluster snapshot_schedule')
    group = argparser.add_mutually_exclusive_group(required=True)
    group.add_argument('--id', dest='cluster_id', help=
        'execute on cluster with this id')
    group.add_argument('--label', dest='label', help=
        'execute on cluster with this label')
    arguments = argparser.parse_args(args)
    return arguments