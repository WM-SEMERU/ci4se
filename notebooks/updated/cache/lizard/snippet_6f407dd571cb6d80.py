def make_path(*path_or_str_or_segments):
    if len(path_or_str_or_segments) == 0:
        return ROOT_PATH
    elif len(path_or_str_or_segments) == 1:
        single_item = path_or_str_or_segments[0]
        if isinstance(single_item, Path):
            return single_item
        if isinstance(single_item, str):
            try:
                return path_parser.parseString(single_item, True).asList()[0]
            except:
                raise ValueError()
        raise TypeError()
    else:
        segments = path_or_str_or_segments
        return sum(map(lambda x: make_path(x), segments), ROOT_PATH)