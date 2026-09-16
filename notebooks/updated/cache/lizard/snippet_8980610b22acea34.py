def use_valgrind(self, tool, xml, console, track_origins, valgrind_extra_params
    ):
    self.valgrind = tool
    self.valgrind_xml = xml
    self.valgrind_console = console
    self.valgrind_track_origins = track_origins
    self.valgrind_extra_params = valgrind_extra_params
    if not tool in ['memcheck', 'callgrind', 'massif']:
        raise AttributeError('Invalid valgrind tool: %s' % tool)