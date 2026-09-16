def _make_builder(config, current_target):
    tool_key = devpipeline_core.toolsupport.choose_tool_key(current_target,
        _BUILD_TOOL_KEYS)
    return devpipeline_core.toolsupport.tool_builder(config, tool_key,
        devpipeline_build.BUILDERS, current_target)