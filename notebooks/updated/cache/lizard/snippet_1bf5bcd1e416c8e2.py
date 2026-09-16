def _sanity_check_args(args):
    if 'scheduler' in args and 'queue' in args:
        if args.scheduler and not args.queue:
            if args.scheduler != 'sge':
                return (
                    'IPython parallel scheduler (-s) specified. This also requires a queue (-q).'
                    )
        elif args.queue and not args.scheduler:
            return (
                'IPython parallel queue (-q) supplied. This also requires a scheduler (-s).'
                )
        elif args.paralleltype == 'ipython' and (not args.queue or not args
            .scheduler):
            return (
                'IPython parallel requires queue (-q) and scheduler (-s) arguments.'
                )