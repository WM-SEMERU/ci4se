def replay_scope(self, sess):
    current_replay = self.replay(sess)
    try:
        self.set_replay(sess, True)
        yield
    finally:
        self.set_replay(sess, current_replay)