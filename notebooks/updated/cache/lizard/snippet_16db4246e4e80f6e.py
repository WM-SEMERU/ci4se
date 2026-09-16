def copyCurrentLayout(self, sourceViewSUID, targetViewSUID, body, verbose=None
    ):
    response = api(url=self.___url + 'apply/layouts/copycat/' + str(
        sourceViewSUID) + '/' + str(targetViewSUID) + '', method='PUT',
        body=body, verbose=verbose)
    return response