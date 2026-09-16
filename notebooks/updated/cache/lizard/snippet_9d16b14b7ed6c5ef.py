def catch_lane_change(self):
    if self.current.lane_name:
        if (self.current.old_lane and self.current.lane_name != self.
            current.old_lane):
            if (self.current.lane_id not in self.current.pool or self.
                current.pool[self.current.lane_id] != self.current.user_id):
                self.current.log.info('LANE CHANGE : %s >> %s' % (self.
                    current.old_lane, self.current.lane_name))
                if self.current.lane_auto_sendoff:
                    self.current.sendoff_current_user()
                self.current.flow_enabled = False
                if self.current.lane_auto_invite:
                    self.current.invite_other_parties(self.
                        _get_possible_lane_owners())
                return True