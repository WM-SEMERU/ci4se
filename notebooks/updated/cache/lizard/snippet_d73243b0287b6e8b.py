def log_local_message(message_format, *args):
    prefix = '{} {}'.format(color('INFO', fg=248), color('request', fg=5))
    message = message_format % args
    sys.stderr.write('{} {}\n'.format(prefix, message))