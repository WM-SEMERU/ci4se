def match_one_pattern(pattern: str, s: str, *args: Optional[Callable], **flags
    ):
    match: Optional[List[str]] = re.findall(pattern, s, **flags)
    if match:
        if len(args) == 0:
            return match
        elif len(args) == 1:
            wrapper, = args
            return [wrapper(m) for m in match]
        else:
            raise TypeError(
                'Multiple wrappers are given! Only one should be given!')
    else:
        print('Pattern "{0}" not found in string {1}!'.format(pattern, s))
        return None