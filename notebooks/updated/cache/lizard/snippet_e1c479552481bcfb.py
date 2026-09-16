def mag_cal_report_send(self, compass_id, cal_mask, cal_status, autosaved,
    fitness, ofs_x, ofs_y, ofs_z, diag_x, diag_y, diag_z, offdiag_x,
    offdiag_y, offdiag_z, force_mavlink1=False):
    return self.send(self.mag_cal_report_encode(compass_id, cal_mask,
        cal_status, autosaved, fitness, ofs_x, ofs_y, ofs_z, diag_x, diag_y,
        diag_z, offdiag_x, offdiag_y, offdiag_z), force_mavlink1=force_mavlink1
        )