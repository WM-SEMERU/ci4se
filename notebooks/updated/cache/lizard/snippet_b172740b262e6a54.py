def setConf(self, conf, type='simu'):
    if conf is None:
        return
    else:
        if isinstance(conf, str):
            conf = MagBlock.str2dict(conf)
        self.setConfDict[type](conf)