def mkdir(self, target_folder):
    self.printv('Making directory: %s' % target_folder)
    self.k.key = re.sub('^/|/$', '', target_folder) + '/'
    self.k.set_contents_from_string('')
    self.k.close()