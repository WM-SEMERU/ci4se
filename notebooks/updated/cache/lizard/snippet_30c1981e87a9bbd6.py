def diagnostic_encode(self, diagFl1, diagFl2, diagFl3, diagSh1, diagSh2,
    diagSh3):
    return MAVLink_diagnostic_message(diagFl1, diagFl2, diagFl3, diagSh1,
        diagSh2, diagSh3)