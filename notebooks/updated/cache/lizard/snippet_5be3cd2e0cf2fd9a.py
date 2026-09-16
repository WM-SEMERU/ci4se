def create_log_inform(self, level_name, msg, name, timestamp=None):
    if timestamp is None:
        timestamp = time.time()
    katcp_version = self.PROTOCOL_INFO.major
    timestamp_msg = ('%.6f' % timestamp if katcp_version >=
        SEC_TS_KATCP_MAJOR else str(int(timestamp * 1000)))
    return Message.inform('log', level_name, timestamp_msg, name, msg)