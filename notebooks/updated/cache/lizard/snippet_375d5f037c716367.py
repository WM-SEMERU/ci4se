def promote_chat_member(self, *args, **kwargs):
    return promote_chat_member(*args, **self._merge_overrides(**kwargs)).run()