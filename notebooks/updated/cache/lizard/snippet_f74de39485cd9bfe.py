def clear_routing_table_entries(self, x, y, app_id):
    arg1 = app_id << 8 | consts.AllocOperations.free_rtr_by_app
    self._send_scp(x, y, 0, SCPCommands.alloc_free, arg1, 1)