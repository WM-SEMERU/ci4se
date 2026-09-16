def get_lines_from_file(filename, lineno, context_lines):

    def get_lines(start, end):
        return [linecache.getline(filename, l).rstrip() for l in range(
            start, end)]
    lower_bound = max(1, lineno - context_lines)
    upper_bound = lineno + context_lines
    linecache.checkcache(filename)
    pre_context = get_lines(lower_bound, lineno)
    context_line = linecache.getline(filename, lineno).rstrip()
    post_context = get_lines(lineno + 1, upper_bound)
    return lower_bound, pre_context, context_line, post_context