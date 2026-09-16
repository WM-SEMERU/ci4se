def total_pages_in(self, leaderboard_name, page_size=None):
    if page_size is None:
        page_size = self.page_size
    return int(math.ceil(self.total_members_in(leaderboard_name) / float(
        page_size)))