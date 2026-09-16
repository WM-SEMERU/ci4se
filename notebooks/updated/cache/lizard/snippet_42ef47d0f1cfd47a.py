def compassmot_status_encode(self, throttle, current, interference,
    CompensationX, CompensationY, CompensationZ):
    return MAVLink_compassmot_status_message(throttle, current,
        interference, CompensationX, CompensationY, CompensationZ)