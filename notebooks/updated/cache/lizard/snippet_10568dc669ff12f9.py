def get_comments_in_range(self, start, end):
    comments = {}
    for rawindex, comment in self.rawdata.extra.comments.items():
        try:
            index = self.get_index_from_base_index(rawindex)
        except IndexError:
            continue
        if index >= start and index < end:
            comments[index] = comment
    return comments