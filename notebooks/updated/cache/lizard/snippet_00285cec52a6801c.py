def master_send_callback(self, m, master):
    if self.status.watch is not None:
        for msg_type in self.status.watch:
            if fnmatch.fnmatch(m.get_type().upper(), msg_type.upper()):
                self.mpstate.console.writeln('> ' + str(m))
                break
    mtype = m.get_type()
    if mtype != 'BAD_DATA' and self.mpstate.logqueue:
        usec = self.get_usec()
        usec = usec & ~3 | 3
        self.mpstate.logqueue.put(bytearray(struct.pack('>Q', usec) + m.
            get_msgbuf()))