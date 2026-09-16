def handle_submit(self):
    form = self.request.form
    uids = form.get('uids')
    container_mapping = self.get_container_mapping()
    for uid in uids:
        src_pos = container_mapping[uid]
        self.context.addDuplicateAnalyses(src_pos)
    redirect_url = '{}/{}'.format(api.get_url(self.context), 'manage_results')
    self.request.response.redirect(redirect_url)