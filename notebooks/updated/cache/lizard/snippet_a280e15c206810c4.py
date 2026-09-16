def pop(self):
    c = self.connection.cursor()
    first_tweet_id = c.execute(
        "SELECT tweet from tweetlist where label='first_tweet'").next()[0]
    if first_tweet_id is None:
        return None
    tweet = c.execute(
        'SELECT id, message, previous_tweet, next_tweet from tweets WHERE id=?'
        , (first_tweet_id,)).next()
    c.execute("UPDATE tweetlist SET tweet=? WHERE label='first_tweet'", (
        tweet[3],))
    if tweet[3] is not None:
        c.execute('UPDATE tweets SET previous_tweet=NULL WHERE id=?', (
            tweet[3],))
    else:
        c.execute('UPDATE tweetlist SET tweet=NULL WHERE label=?', (
            'last_tweet',))
    c.execute('DELETE FROM tweets WHERE id=?', (first_tweet_id,))
    self.connection.commit()
    c.close()
    return tweet[1]