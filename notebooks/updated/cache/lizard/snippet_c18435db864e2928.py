def outLineReceived(self, line):
    log_debug('<<< {name} stdout >>> {line}', name=self.name, line=self.
        outFilter(line))