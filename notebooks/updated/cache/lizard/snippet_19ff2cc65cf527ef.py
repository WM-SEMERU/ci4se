def _pick_best_fit(self, content):
    import math
    for version in range(1, 41):
        capacity = tables.data_capacity[version][self.error][self.mode_num]
        if self.mode_num == tables.modes['kanji'] and capacity >= math.ceil(
            len(content) / 2):
            return version
        if capacity >= len(content):
            return version
    raise ValueError(
        'The data will not fit in any QR code version with the given encoding and error level.'
        )