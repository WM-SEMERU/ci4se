def can_edit_post(self, post, user):
    checker = self._get_checker(user)
    is_author = self._is_post_author(post, user)
    can_edit = user.is_superuser or is_author and checker.has_perm(
        'can_edit_own_posts', post.topic.forum
        ) and not post.topic.is_locked or checker.has_perm('can_edit_posts',
        post.topic.forum)
    return can_edit