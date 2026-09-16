def _compute_mean_on_rock(self, C, mag, rrup, rvol, hypo_depth, CN, CR, f4HW):
    lnSA_AB = C['c1'] + C['c4as'] * (mag - 6) + C['c3as'] * (8.5 - mag
        ) ** 2 + C['c5'] * rrup + (C['c8'] + C['c6as'] * (mag - 6)) * np.log(
        (rrup ** 2 + C['c10as'] ** 2) ** 0.5) + C['c46'] * rvol + C['c32'
        ] * CN + C['c33as'] * CR + f4HW
    return lnSA_AB