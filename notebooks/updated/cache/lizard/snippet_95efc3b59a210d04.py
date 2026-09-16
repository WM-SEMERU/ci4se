def submit_selected(self, btnName=None, update_state=True, *args, **kwargs):
    self.get_current_form().choose_submit(btnName)
    referer = self.get_url()
    if referer is not None:
        if 'headers' in kwargs:
            kwargs['headers']['Referer'] = referer
        else:
            kwargs['headers'] = {'Referer': referer}
    resp = self.submit(self.__state.form, *args, url=self.__state.url, **kwargs
        )
    if update_state:
        self.__state = _BrowserState(page=resp.soup, url=resp.url, request=
            resp.request)
    return resp