def backup(self, filename='backup.zip', attachments=False):
    if self.deploymentType == 'Cloud':
        url = self._options['server'] + '/rest/backup/1/export/runbackup'
        payload = json.dumps({'cbAttachments': attachments})
        self._options['headers']['X-Requested-With'] = 'XMLHttpRequest'
    else:
        url = self._options['server'] + '/secure/admin/XmlBackup.jspa'
        payload = {'filename': filename}
    try:
        r = self._session.post(url, headers=self._options['headers'], data=
            payload)
        if r.status_code == 200:
            return True
        else:
            logging.warning('Got %s response from calling backup.' % r.
                status_code)
            return r.status_code
    except Exception as e:
        logging.error('I see %s', e)