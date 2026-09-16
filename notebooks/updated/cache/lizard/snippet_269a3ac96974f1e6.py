def next_state(self):
    if self.roaster.get_roaster_state() == 'roasting':
        self.roaster.time_remaining = 20
        self.roaster.cool()
    elif self.roaster.get_roaster_state() == 'cooling':
        self.roaster.idle()