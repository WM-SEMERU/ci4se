def verify_multi(self, otp_list, max_time_window=DEFAULT_MAX_TIME_WINDOW,
    sl=None, timeout=None):
    otps = []
    for otp in otp_list:
        otps.append(OTP(otp, self.translate_otp))
    if len(otp_list) < 2:
        raise ValueError('otp_list needs to contain at least two OTPs')
    device_ids = set()
    for otp in otps:
        device_ids.add(otp.device_id)
    if len(device_ids) != 1:
        raise Exception('OTPs contain different device ids')
    for otp in otps:
        response = self.verify(otp.otp, True, sl, timeout, return_response=True
            )
        if not response:
            return False
        otp.timestamp = int(response['timestamp'])
    count = len(otps)
    delta = otps[count - 1].timestamp - otps[0].timestamp
    delta = delta / 8
    if delta < 0:
        raise Exception(
            'delta is smaller than zero. First OTP appears to be older than the last one'
            )
    if delta > max_time_window:
        raise Exception(
            'More than %s seconds have passed between generating the first and the last OTP.'
             % max_time_window)
    return True