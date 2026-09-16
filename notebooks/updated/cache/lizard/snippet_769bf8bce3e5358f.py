def exportItem(self, title, itemId, exportFormat, tags='export', snippet=
    None, exportParameters=None, wait=True):
    url = '%s/export' % self.location
    params = {'f': 'json', 'title': title, 'tags': tags, 'itemId': itemId,
        'exportFormat': exportFormat}
    if snippet is not None:
        params['snippet'] = snippet
    if exportParameters is not None:
        params['exportParameters'] = json.dumps(exportParameters)
    res = self._post(url=url, param_dict=params, securityHandler=self.
        _securityHandler, proxy_port=self._proxy_port, proxy_url=self.
        _proxy_url)
    itemURL = '%s/items/%s' % (self.location, res['exportItemId'])
    if self.currentFolder is not None or self.currentFolder['title'] != 'root':
        self.moveItems(items=res['exportItemId'], folder=self.currentFolder
            ['id'])
    ui = UserItem(url=itemURL, securityHandler=self._securityHandler,
        proxy_url=self._proxy_url, proxy_port=self._proxy_port)
    if wait == True:
        status = 'partial'
        while status != 'completed':
            status = ui.status(jobId=res['jobId'], jobType='export')
            if status['status'] == 'failed':
                raise Exception('Could not export item: %s' % itemId)
            elif status['status'].lower() == 'completed':
                break
            time.sleep(2)
    else:
        return res['jobId'], ui
    return ui