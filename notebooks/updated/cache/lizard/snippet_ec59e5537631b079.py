def sync(self, sync_item, client=None, clientId=None):
    if not client and not clientId:
        clientId = X_PLEX_IDENTIFIER
    if not client:
        for device in self.devices():
            if device.clientIdentifier == clientId:
                client = device
                break
        if not client:
            raise BadRequest('Unable to find client by clientId=%s', clientId)
    if 'sync-target' not in client.provides:
        raise BadRequest('Received client doesn`t provides sync-target')
    params = {'SyncItem[title]': sync_item.title, 'SyncItem[rootTitle]':
        sync_item.rootTitle, 'SyncItem[metadataType]': sync_item.
        metadataType, 'SyncItem[machineIdentifier]': sync_item.
        machineIdentifier, 'SyncItem[contentType]': sync_item.contentType,
        'SyncItem[Policy][scope]': sync_item.policy.scope,
        'SyncItem[Policy][unwatched]': str(int(sync_item.policy.unwatched)),
        'SyncItem[Policy][value]': str(sync_item.policy.value if hasattr(
        sync_item.policy, 'value') else 0), 'SyncItem[Location][uri]':
        sync_item.location, 'SyncItem[MediaSettings][audioBoost]': str(
        sync_item.mediaSettings.audioBoost),
        'SyncItem[MediaSettings][maxVideoBitrate]': str(sync_item.
        mediaSettings.maxVideoBitrate),
        'SyncItem[MediaSettings][musicBitrate]': str(sync_item.
        mediaSettings.musicBitrate),
        'SyncItem[MediaSettings][photoQuality]': str(sync_item.
        mediaSettings.photoQuality),
        'SyncItem[MediaSettings][photoResolution]': sync_item.mediaSettings
        .photoResolution, 'SyncItem[MediaSettings][subtitleSize]': str(
        sync_item.mediaSettings.subtitleSize),
        'SyncItem[MediaSettings][videoQuality]': str(sync_item.
        mediaSettings.videoQuality),
        'SyncItem[MediaSettings][videoResolution]': sync_item.mediaSettings
        .videoResolution}
    url = SyncList.key.format(clientId=client.clientIdentifier)
    data = self.query(url, method=self._session.post, headers={
        'Content-type': 'x-www-form-urlencoded'}, params=params)
    return SyncItem(self, data, None, clientIdentifier=client.clientIdentifier)