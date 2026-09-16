def clean_comment(self):
    comment = self.cleaned_data['text']
    if settings.COMMENTS_ALLOW_PROFANITIES is False:
        bad_words = [w for w in settings.PROFANITIES_LIST if w in comment.
            lower()]
        if bad_words:
            raise forms.ValidationError(ungettext(
                'Watch your mouth! The word %s is not allowed here.',
                'Watch your mouth! The words %s are not allowed here.', len
                (bad_words)) % get_text_list([('"%s%s%s"' % (i[0], '-' * (
                len(i) - 2), i[-1])) for i in bad_words], ugettext('and')))
    return comment