def get_post(self):
    pk = self.kwargs.get(self.post_pk_url_kwarg, None)
    if not pk:
        return
    if not hasattr(self, '_forum_post'):
        self._forum_post = get_object_or_404(Post, pk=pk)
    return self._forum_post