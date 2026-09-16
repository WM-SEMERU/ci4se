def start(self, retry_limit=None):
    wrapper_listener = TweepyWrapperListener(listener=self.listener)
    stream = tweepy.Stream(auth=self.client.tweepy_api.auth, listener=
        wrapper_listener)
    retry_counter = 0
    while retry_limit is None or retry_counter <= retry_limit:
        try:
            retry_counter += 1
            if not self.client.config.get('user_stream'):
                logging.info('Listening to public stream')
                stream.filter(follow=self.filter.follow, track=self.filter.
                    track)
            else:
                if self.filter.follow:
                    logging.warning(
                        "Follow filters won't be used in user stream")
                logging.info('Listening to user stream')
                stream.userstream(track=self.filter.track)
        except AttributeError as e:
            if "'NoneType' object has no attribute 'strip'" in str(e):
                pass
            else:
                raise