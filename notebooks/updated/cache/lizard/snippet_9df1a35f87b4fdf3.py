def cmd_average_waiting_time(self):
    average = [line.time_wait_queues for line in self._valid_lines if line.
        time_wait_queues >= 0]
    divisor = float(len(average))
    if divisor > 0:
        return sum(average) / float(len(average))
    return 0