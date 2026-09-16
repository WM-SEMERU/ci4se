def cancelSignalNotification(self, rule_id):
    if self._signalRules and rule_id in self._signalRules:
        self.objHandler.conn.delMatch(rule_id)
        self._signalRules.remove(rule_id)