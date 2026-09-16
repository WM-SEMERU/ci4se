def get_end_time_str(self):
    try:
        return self.end_datetime.strftime(self.end_time_format)
    except AttributeError:
        return self.NOT_A_TIME_STR