def broaden_eps(dielectric, sigma):
    e = dielectric[0]
    diff = [(e[i + 1] - e[i]) for i in range(len(e) - 1)]
    diff_avg = sum(diff) / len(diff)
    real = [gaussian_filter1d(np.array(dielectric[1])[:, (x)], sigma /
        diff_avg) for x in range(6)]
    imag = [gaussian_filter1d(np.array(dielectric[2])[:, (x)], sigma /
        diff_avg) for x in range(6)]
    return e, np.array(real).T, np.array(imag).T