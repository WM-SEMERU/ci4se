def get_announcements(self, **kwargs):
    from canvasapi.discussion_topic import DiscussionTopic
    return PaginatedList(DiscussionTopic, self.__requester, 'GET',
        'announcements', _kwargs=combine_kwargs(**kwargs))