def record_config(self, rec_opt):
    ret = self.command('configManager.cgi?action=setConfig&{0}'.format(rec_opt)
        )
    return ret.content.decode('utf-8')