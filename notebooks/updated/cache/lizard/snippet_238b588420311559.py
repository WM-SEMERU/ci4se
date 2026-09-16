def ac_viz(acdata):
    acdata = np.log(acdata + 1e-06)
    acdata[:, :, (acdata.shape[2] / 2)] = acdata[:, :, (acdata.shape[2] / 2 -
        1)]
    acdata[:, :, (acdata.shape[2] - 1)] = np.max(acdata)
    return acdata