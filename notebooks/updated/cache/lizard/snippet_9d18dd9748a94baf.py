def query_base_timer(self):
    _, _, time = unpack('<ccI', self.con.send_xid_command('e3', 6))
    return time