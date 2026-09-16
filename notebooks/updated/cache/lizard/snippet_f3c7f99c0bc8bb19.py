def fast_combine_pairs(files, force_single, full_name, separators):
    files = sort_filenames(files)
    chunks = tz.sliding_window(10, files)
    pairs = [combine_pairs(chunk, force_single, full_name, separators) for
        chunk in chunks]
    pairs = [y for x in pairs for y in x]
    longest = defaultdict(list)
    for pair in pairs:
        for file in pair:
            if len(longest[file]) < len(pair):
                longest[file] = pair
    longest = {tuple(sort_filenames(x)) for x in longest.values()}
    return [sort_filenames(list(x)) for x in longest]