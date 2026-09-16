def form_valid(self, post_form, attachment_formset, poll_option_formset, **
    kwargs):
    save_poll_option_formset = (poll_option_formset is not None and not
        self.preview)
    valid = super().form_valid(post_form, attachment_formset,
        poll_option_formset=poll_option_formset, **kwargs)
    if save_poll_option_formset:
        poll_option_formset.topic = self.forum_post.topic
        poll_option_formset.save(poll_question=post_form.cleaned_data.pop(
            'poll_question', None), poll_max_options=post_form.cleaned_data
            .pop('poll_max_options', None), poll_duration=post_form.
            cleaned_data.pop('poll_duration', None), poll_user_changes=
            post_form.cleaned_data.pop('poll_user_changes', None))
    return valid