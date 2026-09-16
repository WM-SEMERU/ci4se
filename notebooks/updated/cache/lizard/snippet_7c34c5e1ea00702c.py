def _get_result_color(self, time_taken):
    time_taken_ms = time_taken * 1000
    if time_taken_ms <= self.timer_ok:
        color = 'green'
    elif time_taken_ms <= self.timer_warning:
        color = 'yellow'
    else:
        color = 'red'
    return color