def mavlink_packet(self, m):
    if m.get_type() == 'SERIAL_CONTROL':
        data = m.data[:m.count]
        if m.count > 0:
            s = ''.join(str(chr(x)) for x in data)
            if self.mpstate.system == 'Windows':
                s = s.replace('\x1b[K', '')
            sys.stdout.write(s)
            self.last_packet = time.time()