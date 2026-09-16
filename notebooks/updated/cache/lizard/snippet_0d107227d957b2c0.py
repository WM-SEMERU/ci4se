def moderate(self, comment, content_object, request):
    if self.akismet_check:
        akismet_result = akismet_check(comment, content_object, request)
        if akismet_result:
            if akismet_result in (SpamStatus.ProbableSpam, SpamStatus.
                DefiniteSpam) and self.akismet_check_action in ('auto',
                'soft_delete', 'delete'):
                comment.is_removed = True
            return True
    if super(FluentCommentsModerator, self).moderate(comment,
        content_object, request):
        return True
    if self.moderate_bad_words:
        input_words = split_words(comment.comment)
        if self.moderate_bad_words.intersection(input_words):
            return True
    if self.akismet_check and self.akismet_check_action not in ('soft_delete',
        'delete'):
        if akismet_check(comment, content_object, request):
            return True
    return False