def diagnostic_send(self, diagFl1, diagFl2, diagFl3, diagSh1, diagSh2,
    diagSh3, force_mavlink1=False):
    return self.send(self.diagnostic_encode(diagFl1, diagFl2, diagFl3,
        diagSh1, diagSh2, diagSh3), force_mavlink1=force_mavlink1)