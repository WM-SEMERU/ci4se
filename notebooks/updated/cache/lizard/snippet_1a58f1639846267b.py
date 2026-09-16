def tell_sender_to_start(self):
    now = time.time()
    if now - self.time_last_start_packet_sent < 1:
        return
    self.time_last_start_packet_sent = now
    if self.log_settings.verbose:
        print('DFLogger: Sending start packet')
    target_sys = self.log_settings.df_target_system
    target_comp = self.log_settings.df_target_component
    self.master.mav.remote_log_block_status_send(target_sys, target_comp,
        mavutil.mavlink.MAV_REMOTE_LOG_DATA_BLOCK_START, 1)