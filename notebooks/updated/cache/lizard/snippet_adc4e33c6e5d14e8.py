def formatted(self, include_server_time):
    if include_server_time:
        return (
            """{0:5d} {1:5d} {2:7.3f} {3:7.3f} {4:7.3f} {5:7.3f} {6:7.3f} {7:7.3f} {8:6.0f} {9:6.0f} {10:6.0f} {11:8.0f} {12:8.0f} {13:8.0f} {14}
"""
            .format(self.count, self.exception_count, self.avg_time, self.
            min_time, self.max_time, self.avg_server_time, self.
            min_server_time, self.max_server_time, self.avg_request_len,
            self.min_request_len, self.max_request_len, self.avg_reply_len,
            self.min_reply_len, self.max_reply_len, self.name))
    else:
        return (
            """{0:5d} {1:5d} {2:7.3f} {3:7.3f} {4:7.3f} {5:6.0f} {6:6.0f} {7:6.0f} {8:6.0f} {9:8.0f} {10:8.0f} {11}
"""
            .format(self.count, self.exception_count, self.avg_time, self.
            min_time, self.max_time, self.avg_request_len, self.
            min_request_len, self.max_request_len, self.avg_reply_len, self
            .min_reply_len, self.max_reply_len, self.name))