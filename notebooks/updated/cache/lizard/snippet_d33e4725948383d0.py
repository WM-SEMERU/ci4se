def equals(self, other, timestamp_delta=1e-06):
    return (self is other or (timestamp_delta is None or abs(self.timestamp -
        other.timestamp) <= timestamp_delta) and self.arbitration_id ==
        other.arbitration_id and self.is_extended_id == other.
        is_extended_id and self.dlc == other.dlc and self.data == other.
        data and self.is_remote_frame == other.is_remote_frame and self.
        is_error_frame == other.is_error_frame and self.channel == other.
        channel and self.is_fd == other.is_fd and self.bitrate_switch ==
        other.bitrate_switch and self.error_state_indicator == other.
        error_state_indicator)