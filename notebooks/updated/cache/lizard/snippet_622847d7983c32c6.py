def parse_errors(csv_file):
    with csv_file.open(newline='') as f:
        f = csv.reader(f)
        next(f, None)
        for line, tup in enumerate(f, start=2):
            try:
                name, codes, description = tup
            except ValueError:
                raise ValueError(
                    'Columns count mismatch, unquoted comma in desc? (line {})'
                    .format(line)) from None
            try:
                codes = [int(x) for x in codes.split()] or [400]
            except ValueError:
                raise ValueError('Not all codes are integers (line {})'.
                    format(line)) from None
            yield Error([int(x) for x in codes], name, description)