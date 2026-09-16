def clear_to_reset(self, config_vars):
    super(ClockManagerSubsystem, self).clear_to_reset(config_vars)
    self.tick_counters = dict(fast=0, user1=0, user2=0, normal=0)
    self.is_utc = False
    self.time_offset = 0
    if self.has_rtc and self.stored_offset is not None:
        self.time_offset = self.stored_offset + self.uptime
    self.uptime = 0
    self.ticks['fast'] = config_vars.get('fast_tick', 0)
    self.ticks['user1'] = config_vars.get('user_tick_1', 0)
    self.ticks['user2'] = config_vars.get('user_tick_2', 0)