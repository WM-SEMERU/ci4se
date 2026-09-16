def visited(self):
    try:
        binfo = self.binfo
    except AttributeError:
        pass
    else:
        self.ninfo.update(self)
        SCons.Node.store_info_map[self.store_info](self)