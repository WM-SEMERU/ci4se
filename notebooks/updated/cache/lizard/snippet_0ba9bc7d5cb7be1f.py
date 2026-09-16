def read(self):
    if self.done_f.done():
        raise BrokenPipeError
    try:
        result = yield From(read_message_from_pipe(self.pipe_instance.
            pipe_handle))
        raise Return(result)
    except BrokenPipeError:
        self.done_f.set_result(None)
        raise