def energy_prof(step):
    diff, rad = diffs_prof(step)
    adv, _ = advts_prof(step)
    return diff + np.append(adv, 0), rad