def pipeRecvConsole(self):
    try:
        while True:
            console_msg = self.parent_pipe_recv_console.recv()
            if console_msg is not None:
                self.console.writeln(console_msg)
            time.sleep(0.1)
    except EOFError:
        pass