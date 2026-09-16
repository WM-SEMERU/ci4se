def get_record_params(args):
    name, rtype, content, ttl, priority = (args.name, args.rtype, args.
        content, args.ttl, args.priority)
    return name, rtype, content, ttl, priority