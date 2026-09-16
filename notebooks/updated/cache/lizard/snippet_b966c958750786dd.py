def PX4_update(IMU, ATT):
    global px4_state
    if px4_state is None:
        px4_state = PX4_State(degrees(ATT.Roll), degrees(ATT.Pitch),
            degrees(ATT.Yaw), IMU._timestamp)
    gyro = Vector3(IMU.GyroX, IMU.GyroY, IMU.GyroZ)
    accel = Vector3(IMU.AccX, IMU.AccY, IMU.AccZ)
    px4_state.update(gyro, accel, IMU._timestamp)
    return px4_state