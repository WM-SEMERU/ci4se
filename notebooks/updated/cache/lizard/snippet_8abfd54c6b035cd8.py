def bash(filename):
    sys.stdout.flush()
    subprocess.call('bash {}'.format(filename), shell=True)