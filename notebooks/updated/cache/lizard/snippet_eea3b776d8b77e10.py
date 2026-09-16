def get_connections_by_dest(self, dest):
    with self._mutex:
        res = []
        for c in self.connections:
            if c.has_port(self) and c.has_port(dest):
                res.append(c)
        return res