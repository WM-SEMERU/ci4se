def get_urlpatterns(self):
    return [path(_('topic/<str:slug>-<int:pk>/lock/'), self.topic_lock_view
        .as_view(), name='topic_lock'), path(_(
        'topic/<str:slug>-<int:pk>/unlock/'), self.topic_unlock_view.
        as_view(), name='topic_unlock'), path(_(
        'topic/<str:slug>-<int:pk>/delete/'), self.topic_delete_view.
        as_view(), name='topic_delete'), path(_(
        'topic/<str:slug>-<int:pk>/move/'), self.topic_move_view.as_view(),
        name='topic_move'), path(_(
        'topic/<str:slug>-<int:pk>/change/topic/'), self.
        topic_update_to_normal_topic_view.as_view(), name=
        'topic_update_to_post'), path(_(
        'topic/<str:slug>-<int:pk>/change/sticky/'), self.
        topic_update_to_sticky_topic_view.as_view(), name=
        'topic_update_to_sticky'), path(_(
        'topic/<str:slug>-<int:pk>/change/announce/'), self.
        topic_update_to_announce_view.as_view(), name=
        'topic_update_to_announce'), path(_('queue/'), self.
        moderation_queue_list_view.as_view(), name='queue'), path(_(
        'queue/<int:pk>/'), self.moderation_queue_detail_view.as_view(),
        name='queued_post'), path(_('queue/<int:pk>/approve/'), self.
        post_approve_view.as_view(), name='approve_queued_post'), path(_(
        'queue/<int:pk>/disapprove/'), self.post_disapprove_view.as_view(),
        name='disapprove_queued_post')]