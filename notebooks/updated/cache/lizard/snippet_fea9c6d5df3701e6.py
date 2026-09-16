def main(sys=sys):
    if len(sys.argv) != 2:
        sys.stderr.write(USAGE)
        return 1
    EliotFilter(sys.argv[1], sys.stdin, sys.stdout).run()
    return 0