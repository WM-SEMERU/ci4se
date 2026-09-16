def assert_count_equal(sequence1, sequence2, msg_fmt='{msg}'):

    def compare():
        missing1 = list(sequence2)
        missing2 = []
        for item in sequence1:
            try:
                missing1.remove(item)
            except ValueError:
                missing2.append(item)
        return missing1, missing2

    def build_message():
        msg = ''
        if missing_from_1:
            msg += 'missing from sequence 1: ' + ', '.join(repr(i) for i in
                missing_from_1)
        if missing_from_1 and missing_from_2:
            msg += '; '
        if missing_from_2:
            msg += 'missing from sequence 2: ' + ', '.join(repr(i) for i in
                missing_from_2)
        return msg
    missing_from_1, missing_from_2 = compare()
    if missing_from_1 or missing_from_2:
        fail(msg_fmt.format(msg=build_message(), first=sequence1, second=
            sequence2))