def _retrieve_problem(self, id_):
    future = Future(self, id_, self.return_matrix, None)
    self.client._poll(future)
    return future