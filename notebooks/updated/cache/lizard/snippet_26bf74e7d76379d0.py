def hessian(self, x, y, center_x=0, center_y=0, **kwargs):
    diff = 1e-06
    alpha_ra, alpha_dec = self.derivatives(x, y, center_x=center_x,
        center_y=center_y, **kwargs)
    alpha_ra_dx, alpha_dec_dx = self.derivatives(x + diff, y, center_x=
        center_x, center_y=center_y, **kwargs)
    alpha_ra_dy, alpha_dec_dy = self.derivatives(x, y + diff, center_x=
        center_x, center_y=center_y, **kwargs)
    dalpha_rara = (alpha_ra_dx - alpha_ra) / diff
    dalpha_radec = (alpha_ra_dy - alpha_ra) / diff
    dalpha_decdec = (alpha_dec_dy - alpha_dec) / diff
    f_xx = dalpha_rara
    f_yy = dalpha_decdec
    f_xy = dalpha_radec
    return f_xx, f_yy, f_xy