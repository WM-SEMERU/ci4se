def get_user_timer(self, index):
    err, tick = self.clock_manager.get_tick(index)
    return [err, tick]