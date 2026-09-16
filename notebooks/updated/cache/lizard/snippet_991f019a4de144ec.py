def main():
    args = parse_input()
    args.lock = True
    args.question = []
    args.all = False
    args.timeout = 0
    args.verbose = False
    args.interactive = False
    try:
        assign = assignment.load_assignment(args.config, args)
        msgs = messages.Messages()
        lock.protocol(args, assign).run(msgs)
    except (ex.LoadingException, ex.SerializeException) as e:
        log.warning('Assignment could not instantiate', exc_info=True)
        print('Error: ' + str(e).strip())
        exit(1)
    except (KeyboardInterrupt, EOFError):
        log.info('Quitting...')
    else:
        assign.dump_tests()