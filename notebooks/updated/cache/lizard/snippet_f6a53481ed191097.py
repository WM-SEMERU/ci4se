def phyper_at_fpr(fg_vals, bg_vals, fpr=0.01):
    fg_vals = np.array(fg_vals)
    s = scoreatpercentile(bg_vals, 100 - fpr * 100)
    table = [[sum(fg_vals >= s), sum(bg_vals >= s)], [sum(fg_vals < s), sum
        (bg_vals < s)]]
    return fisher_exact(table, alternative='greater')[1]