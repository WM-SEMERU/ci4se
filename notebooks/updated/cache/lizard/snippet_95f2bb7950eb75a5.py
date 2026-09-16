def get_account_details(self, account):
    _form = mechanize.HTMLForm(self.SEARCH_MEMBERS_URL, method='POST')
    _form.new_control('text', 'username', {'value': account})
    _form.new_control('text', '_', {'value': ''})
    try:
        r = self.post_url(self.SEARCH_MEMBERS_URL, form=_form)
    except AuthRequiredException:
        self._auth()
        r = self.post_url(self.SEARCH_MEMBERS_URL, form=_form)
    if r:
        _decoded = json.loads(r.replace("'", '"'))
        if _decoded[0]:
            return _decoded[0][0]
    raise InvalidAccountException