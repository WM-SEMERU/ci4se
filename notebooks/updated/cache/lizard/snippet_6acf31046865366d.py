def list_users(self):
    folders = glob('%s/*' % self.database)
    folders.sort()
    return [self.print_user(x) for x in folders]