def _show_retry_warning(host):
    sys.stderr.write('\nConnection to {} failed. Retrying.\n'.format(host))
    sys.stderr.flush()