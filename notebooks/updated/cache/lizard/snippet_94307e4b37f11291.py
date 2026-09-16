def wait_for_alt(self, alt, epsilon=0.1, rel=True, timeout=None):

    def get_alt():
        if rel:
            alt = self.location.global_relative_frame.alt
        else:
            alt = self.location.global_frame.alt
        return alt

    def check_alt():
        cur = get_alt()
        delta = abs(alt - cur)
        return delta < epsilon or cur > alt > start or cur < alt < start
    start = get_alt()
    self.wait_for(check_alt, timeout=timeout, errmsg=
        'failed to reach specified altitude')