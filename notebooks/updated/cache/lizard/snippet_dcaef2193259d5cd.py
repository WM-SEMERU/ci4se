def get_var_type(self, name):
    method = 'get_var_type'
    A = None
    metadata = {method: name}
    send_array(self.socket, A, metadata)
    A, metadata = recv_array(self.socket, poll=self.poll, poll_timeout=self
        .poll_timeout, flags=self.zmq_flags)
    return metadata[method]