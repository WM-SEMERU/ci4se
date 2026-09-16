def angledependentabsorption(twotheta, transmission):
    cor = np.ones(twotheta.shape)
    if transmission == 1:
        return cor
    mud = -np.log(transmission)
    cor[twotheta > 0] = transmission * mud * (1 - 1 / np.cos(twotheta[
        twotheta > 0])) / (np.exp(-mud / np.cos(twotheta[twotheta > 0])) -
        np.exp(-mud))
    return cor