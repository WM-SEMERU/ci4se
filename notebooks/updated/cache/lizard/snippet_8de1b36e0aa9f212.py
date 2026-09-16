def ekf1_pos(EKF1):
    global ekf_home
    from . import mavutil
    self = mavutil.mavfile_global
    if ekf_home is None:
        if not 'GPS' in self.messages or self.messages['GPS'].Status != 3:
            return None
        ekf_home = self.messages['GPS']
        ekf_home.Lat, ekf_home.Lng = gps_offset(ekf_home.Lat, ekf_home.Lng,
            -EKF1.PE, -EKF1.PN)
    lat, lon = gps_offset(ekf_home.Lat, ekf_home.Lng, EKF1.PE, EKF1.PN)
    return lat, lon