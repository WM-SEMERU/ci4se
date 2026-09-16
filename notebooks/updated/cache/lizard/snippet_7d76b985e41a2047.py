def run_command(cmd, debug=False):
    if debug:
        msg = '  PWD: {}'.format(os.getcwd())
        print_warn(msg)
        msg = '  COMMAND: {}'.format(cmd)
        print_warn(msg)
    cmd()