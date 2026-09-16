def open_subreddit_page(self, name):
    from .subreddit_page import SubredditPage
    with self.term.loader('Loading subreddit'):
        page = SubredditPage(self.reddit, self.term, self.config, self.
            oauth, name)
    if not self.term.loader.exception:
        return page