def get_source_qq_data(id=None):
    sdata = ui.get_data(id=id)
    kev = sdata.get_x()
    obs_data = sdata.counts
    model_data = ui.get_model(id=id)(kev)
    return np.vstack((kev, obs_data, model_data))