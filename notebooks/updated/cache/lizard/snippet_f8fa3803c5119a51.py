def Start(self):
    self.Init()
    fd = aff4.FACTORY.Open(self.args.vfs_file_urn, mode='rw', token=self.token)
    if fd.Get(fd.Schema.TYPE) is None:
        fd = fd.Upgrade(standard.VFSDirectory)
    self.state.get_file_flow_urn = fd.Update(attribute=self.args.attribute)