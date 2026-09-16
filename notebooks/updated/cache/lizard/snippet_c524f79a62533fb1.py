def report_unknown(bytes_so_far, total_size, speed, eta):
    sys.stdout.write('Downloading: {0} / Unknown - {1}/s      '.format(
        approximate_size(bytes_so_far), approximate_size(speed)))
    sys.stdout.write('\r')
    sys.stdout.flush()