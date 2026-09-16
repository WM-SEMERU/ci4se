def _log_message(self, level, process_name, timeperiod, msg):
    self.timetable.add_log_entry(process_name, timeperiod, msg)
    self.logger.log(level, msg)