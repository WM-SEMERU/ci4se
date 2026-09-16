def die(*messages):
    sys.stderr.write('%s.%s: ' % get_caller_info(trace=True))
    sys.stderr.write(' '.join(map(str, messages)))
    sys.stderr.write('\n')
    sys.exit(1)