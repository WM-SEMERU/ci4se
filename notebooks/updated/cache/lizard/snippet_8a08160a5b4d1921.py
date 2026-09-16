def wait_for_any_log(nodes, pattern, timeout, filename='system.log', marks=None
    ):
    if marks is None:
        marks = {}
    for _ in range(timeout):
        for node in nodes:
            found = node.grep_log(pattern, filename=filename, from_mark=
                marks.get(node, None))
            if found:
                return node
        time.sleep(1)
    raise TimeoutError(time.strftime('%d %b %Y %H:%M:%S', time.gmtime()) +
        ' Unable to find: ' + repr(pattern) + ' in any node log within ' +
        str(timeout) + 's')