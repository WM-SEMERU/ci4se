def cmd_generate(args):
    if args.start:
        if args.end or args.reply:
            raise ValueError('multiple input arguments')
        args.reply_to = args.start
        args.reply_mode = ReplyMode.END
    elif args.end:
        if args.reply:
            raise ValueError('multiple input arguments')
        args.reply_to = args.end
        args.reply_mode = ReplyMode.START
    elif args.reply:
        args.reply_to = args.reply
        args.reply_mode = ReplyMode.REPLY
    else:
        args.reply_to = None
        args.reply_mode = ReplyMode.END
    markov = load(MarkovText, args.state, args)
    ss = range(args.count)
    if args.progress:
        title = truncate(args.output.name, BAR_DESC_SIZE - 1, False)
        ss = tqdm(ss, desc=title, bar_format=BAR_FORMAT, dynamic_ncols=True)
    if not args.format:
        markov.formatter = lambda x: x
    for _ in ss:
        data = markov(args.words, state_size=args.state_size, reply_to=args
            .reply_to, reply_mode=args.reply_mode)
        if data:
            print(data)