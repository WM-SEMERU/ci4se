def load_full_command_table(self):
    load_cmd_tbl_func = self.kwargs.get('load_cmd_tbl_func', lambda _: {})
    cache_reserved_commands(load_cmd_tbl_func)
    telemetry.set_full_command_table_loaded()