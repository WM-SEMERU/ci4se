def email_message(self):
    url = settings.SITE_URL
    hello_text = __('Hi %s,' % self.to_user.get_full_name())
    action_text = __('\n\nMore details here: %s') % url
    explain_text = __(
        """This is an automatic notification sent from from %s.
If you want to stop receiving this notification edit youremail notification settings here: %s"""
        ) % (settings.SITE_NAME, 'TODO')
    return '%s\n\n%s%s\n\n%s' % (hello_text, self.text, action_text,
        explain_text)