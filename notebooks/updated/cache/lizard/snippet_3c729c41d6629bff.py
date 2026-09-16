def reportSuspiciousNodeEx(self, ex: SuspiciousNode):
    self.reportSuspiciousNode(ex.node, ex.reason, ex.code, ex.offendingMsg)