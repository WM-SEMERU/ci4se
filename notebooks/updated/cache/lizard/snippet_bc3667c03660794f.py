def accept(self, logevent):
    if self.components and logevent.component not in self.components:
        return False
    if self.levels and logevent.level not in self.levels:
        return False
    if self.namespaces and logevent.namespace not in self.namespaces:
        return False
    if self.commands and logevent.command not in self.commands:
        return False
    if self.operations and logevent.operation not in self.operations:
        return False
    if self.threads:
        if (logevent.thread not in self.threads and logevent.conn not in
            self.threads):
            return False
    if self.pattern and logevent.pattern != self.pattern:
        return False
    if self.planSummaries and logevent.planSummary not in self.planSummaries:
        return False
    return True