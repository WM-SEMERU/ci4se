def csv_dict(d):
    if len(d) == 0:
        return '{}'
    return '{' + ', '.join(["'{}': {}".format(k, quotable(v)) for k, v in d
        .items()]) + '}'