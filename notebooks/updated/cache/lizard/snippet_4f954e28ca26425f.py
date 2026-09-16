def compile_master(self):
    load = {'grains': self.grains, 'opts': self.opts, 'cmd': '_master_state'}
    try:
        return self.channel.send(load, tries=3, timeout=72000)
    except SaltReqTimeoutError:
        return {}