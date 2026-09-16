def invoke_task(task, args):
    parser, proxy_args = get_task_parser(task)
    if proxy_args:
        return task(*args)
    else:
        pargs = parser.parse_args(args)
        return task(**vars(pargs))