def delete_attachment(self, attachment, headers=None):
    self.fetch()
    attachment_url = '/'.join((self.document_url, attachment))
    if headers is None:
        headers = {'If-Match': self['_rev']}
    else:
        headers['If-Match'] = self['_rev']
    resp = self.r_session.delete(attachment_url, headers=headers)
    resp.raise_for_status()
    super(Document, self).__setitem__('_rev', response_to_json_dict(resp)[
        'rev'])
    if self.get('_attachments'):
        if self['_attachments'].get(attachment):
            self['_attachments'].__delitem__(attachment)
        if not self['_attachments']:
            super(Document, self).__delitem__('_attachments')
    return response_to_json_dict(resp)