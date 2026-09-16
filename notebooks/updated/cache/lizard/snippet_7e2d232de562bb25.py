def run_score(self):
    diffs = 0
    lines = 0
    for file in self.files:
        try:
            results = self._check(file)
        except Error as e:
            termcolor.cprint(e.msg, 'yellow', file=sys.stderr)
            continue
        diffs += results.diffs
        lines += results.lines
    try:
        print(max(1 - diffs / lines, 0.0))
    except ZeroDivisionError:
        print(0.0)