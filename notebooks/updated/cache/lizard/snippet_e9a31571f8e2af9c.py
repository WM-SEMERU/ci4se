def update_roster(self, REQUEST=None):
    CheckAuthenticator(self.request)
    PostOnly(self.request)
    form = self.request.form
    entries = form.get('entries', [])
    self.update_users(entries)
    api.portal.show_message(message=_('Roster updated.'), request=self.request)
    return self.request.response.redirect('%s/@@edit-roster' % self.context
        .absolute_url())