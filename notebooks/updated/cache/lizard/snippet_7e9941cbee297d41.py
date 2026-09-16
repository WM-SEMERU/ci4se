def cmd_link_add(self, args):
    descriptor = args[0]
    print('Adding link %s' % descriptor)
    self.link_add(descriptor)