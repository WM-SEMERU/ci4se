def get_submit_args(args):
    submit_args = dict(testrun_id=args.testrun_id, user=args.user, password
        =args.password, no_verify=args.no_verify, verify_timeout=args.
        verify_timeout, log_file=args.job_log, dry_run=args.dry_run)
    submit_args = {k: v for k, v in submit_args.items() if v is not None}
    return Box(submit_args, frozen_box=True, default_box=True)