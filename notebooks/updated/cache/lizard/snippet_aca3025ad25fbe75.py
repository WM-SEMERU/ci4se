def collect(self):
    ret = super(Command, self).collect()
    if settings.threads:
        Pool(settings.threads).map(self.do_copy_file, self.tasks)
    return ret