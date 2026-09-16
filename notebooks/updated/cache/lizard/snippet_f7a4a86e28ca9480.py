def tool_builder(component, key, tool_map, *args):
    tool_name = component.get(key)
    if tool_name:
        tool_fn = tool_map.get(tool_name)
        if tool_fn:
            return tool_fn[0](*args)
        raise Exception("Unknown {} '{}' for {}".format(key, tool_name,
            component.name))
    raise MissingToolKey(key, component)