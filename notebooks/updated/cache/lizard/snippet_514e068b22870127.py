def audio_load_time(self):
    load_times = self.get_load_times('audio')
    return round(mean(load_times), self.decimal_precision)