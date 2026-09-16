def set_save_itrs_root(setting):
    setting = bool(setting)
    f.root.times.save_itrs = setting
    return setting