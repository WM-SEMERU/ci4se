def _disconnect(cls):
    post_save.disconnect(notify_items, sender=cls, dispatch_uid=
        'knocker_{0}'.format(cls.__name__))