def plot_rebit_modelparams(modelparams, rebit_axes=REBIT_AXES, **kwargs):
    mps = modelparams[:, (rebit_axes)] * np.sqrt(2)
    plt.scatter(mps[:, (0)], mps[:, (1)], **kwargs)