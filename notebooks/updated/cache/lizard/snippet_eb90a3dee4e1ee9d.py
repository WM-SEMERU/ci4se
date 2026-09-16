def data_log_send(self, fl_1, fl_2, fl_3, fl_4, fl_5, fl_6, force_mavlink1=
    False):
    return self.send(self.data_log_encode(fl_1, fl_2, fl_3, fl_4, fl_5,
        fl_6), force_mavlink1=force_mavlink1)