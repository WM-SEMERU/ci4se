def hide_tool(self, context_name, tool_name):
    data = self._context(context_name)
    hidden_tools = data['hidden_tools']
    if tool_name not in hidden_tools:
        self._validate_tool(context_name, tool_name)
        hidden_tools.add(tool_name)
        self._flush_tools()