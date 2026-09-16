def main():
    args = _parse_args()
    _init_logging(args.verbose)
    client = _from_args(args)
    client.submit_error(args.description, args.extra, default_message=args.
        default_message)