def debug(self, debug_commands):
    if isinstance(debug_commands, sc_debug.DebugCommand):
        debug_commands = [debug_commands]
    return self._client.send(debug=sc_pb.RequestDebug(debug=debug_commands))