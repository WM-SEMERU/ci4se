def _decode_time_rotation_index(self, time_rot_index):
    time_index_decode_table = {'year': 0, 'years': 0, 'tm_year': 0, 'month':
        1, 'months': 1, 'tm_mon': 1, 'day': 2, 'days': 2, 'tm_mday': 2,
        'hour': 3, 'hours': 3, 'tm_hour': 3, 'minute': 4, 'minutes': 4,
        'tm_min': 4, 'second': 5, 'seconds': 5, 'tm_sec': 5}
    if time_rot_index not in time_index_decode_table.keys():
        raise ValueError('Invalid time option specified for log rotation')
    return time_index_decode_table[time_rot_index]