def waypoint_count_send(self, seq):
    if self.mavlink10():
        self.mav.mission_count_send(self.target_system, self.
            target_component, seq)
    else:
        self.mav.waypoint_count_send(self.target_system, self.
            target_component, seq)