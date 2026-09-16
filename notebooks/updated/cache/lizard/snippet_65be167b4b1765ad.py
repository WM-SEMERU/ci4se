def setup_users_signals(self):
    log.debug('Setting up users page signals.')
    self.users_user_view_pb.clicked.connect(self.users_view_user)
    self.users_user_create_pb.clicked.connect(self.create_user)