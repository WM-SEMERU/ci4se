def clear_port_stats(self):
    stat = IxeStat(self)
    stat.ix_set_default()
    stat.enableValidStats = True
    stat.ix_set()
    stat.write()