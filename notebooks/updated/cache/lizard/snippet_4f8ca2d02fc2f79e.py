def _interactive_mode(interactive_flag=False):
    return any([interactive_flag, sys.flags.interactive, len(sys.argv) <= 1])