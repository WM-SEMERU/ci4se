def gen_cannon_grad_spec(choose, coeffs, pivots):
    base_labels = [4800, 2.5, 0.03, 0.1, -0.17, -0.17, 0, -0.16, -0.13, -
        0.15, 0.13, 0.08, 0.17, -0.062]
    label_names = np.array(['TEFF', 'LOGG', 'AK', 'Al', 'Ca', 'C', 'Fe',
        'Mg', 'Mn', 'Ni', 'N', 'O', 'Si', 'Ti'])
    label_atnum = np.array([0, 1, -1, 13, 20, 6, 26, 12, 25, 28, 7, 8, 14, 22])
    ind = np.where(label_atnum == choose)[0][0]
    low_lab = copy.copy(base_labels)
    high = base_labels[ind]
    if choose > 0:
        low = base_labels[ind] - 0.2
    else:
        if choose != 0:
            print('warning...')
        low = base_labels[ind] - 200
    low_lab[ind] = low
    lvec = train_model._get_lvec(np.array([low_lab]), pivots)[0]
    model_low = np.dot(coeffs, lvec)
    lvec = train_model._get_lvec(np.array([base_labels]), pivots)[0]
    model_high = np.dot(coeffs, lvec)
    grad_spec = (model_high - model_low) / (high - low)
    return grad_spec