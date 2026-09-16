def Get(self, key):
    for alert in self.alerts:
        if alert.id == key:
            return alert
        elif alert.name == key:
            return alert