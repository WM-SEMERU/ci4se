def add_tags(self, tags):
    if isinstance(tags, (str, unicode)):
        tags = [tags]
    objs = object_session(self)
    tmps = [FeedTag(tag=t, feed=self) for t in tags]
    objs.add_all(tmps)
    objs.commit()