def format_uncertainty(value, uncertianty, scinotn_break=4):
    if uncertianty == 0:
        return '{0:f}'.format(value)
    else:
        mag_unc = int(np.log10(np.abs(uncertianty)))
        mag_val = int(np.log10(np.abs(value))) if value != 0 else 0
        n_digits = max(mag_val - mag_unc, 0)
        if abs(mag_val) < abs(mag_unc) and abs(mag_unc) > scinotn_break:
            scale = 10 ** mag_unc
            return '({{0:0.{0}f}} \\pm {{1:0.{0}f}}) \\times 10^{{2}}'.format(
                n_digits).format(value / scale, uncertianty / scale, mag_unc)
        if abs(mag_val) <= scinotn_break:
            return '{{0:0.{n_digits}f}} \\pm {{1:0.{n_digits}f}}'.format(
                n_digits=n_digits).format(value, uncertianty)
        else:
            scale = 10 ** mag_val
            return '({{0:0.{0}f}} \\pm {{1:0.{0}f}}) \\times 10^{{2}}'.format(
                n_digits).format(value / scale, uncertianty / scale, mag_val)