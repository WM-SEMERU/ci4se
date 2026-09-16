def preload_defs(self):
    for d in (self.module.search('grouping') + self.module.search('typedef')):
        uname, dic = self.unique_def_name(d)
        self.install_def(uname, d, dic)