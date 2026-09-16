def rotation(ATTITUDE):
    r = Matrix3()
    r.from_euler(ATTITUDE.roll, ATTITUDE.pitch, ATTITUDE.yaw)
    return r