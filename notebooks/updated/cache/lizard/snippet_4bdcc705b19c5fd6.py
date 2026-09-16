def run(self, fetch_list, feed_dict=None, sess=None):
    if tf.get_default_graph() != self._graph:
        raise ValueError(
            'The current default graph is different from the graph used at construction time of RecurrentRunner.'
            )
    if feed_dict is None:
        all_feeds_dict = {}
    else:
        all_feeds_dict = dict(feed_dict)
    all_feeds_dict.update(self._state_feeds)
    all_fetches_list = list(fetch_list)
    all_fetches_list += self._state_fetches
    sess = sess or tf.get_default_session()
    fetches = sess.run(all_fetches_list, all_feeds_dict)
    states = fetches[len(fetch_list):]
    for i, s in enumerate(states):
        self._state_feeds[self._state_feed_names[i]] = s
    return fetches[:len(fetch_list)]