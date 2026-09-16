def _write_named_sockets(self, socket_map):
    for socket_name, socket_info in socket_map.items():
        self.write_named_socket(socket_name, socket_info)