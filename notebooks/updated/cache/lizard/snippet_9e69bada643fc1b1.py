def download_to_file(self, file):
    con = ConnectionManager().get_connection(self._connection_alias)
    return con.download_to_file(self.file, file, append_base_url=False)