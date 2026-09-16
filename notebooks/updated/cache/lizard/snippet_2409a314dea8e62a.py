def _tool_from_string(name):
    known_tools = sorted(_known_tools.keys())
    if name in known_tools:
        tool_fn = _known_tools[name]
        if isinstance(tool_fn, string_types):
            tool_fn = _known_tools[tool_fn]
        return tool_fn()
    else:
        matches, text = difflib.get_close_matches(name.lower(), known_tools
            ), 'similar'
        if not matches:
            matches, text = known_tools, 'possible'
        raise ValueError("unexpected tool name '%s', %s tools are %s" % (
            name, text, nice_join(matches)))