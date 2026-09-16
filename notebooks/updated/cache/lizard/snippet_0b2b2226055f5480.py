def get(self, sid):
    return AssetVersionContext(self._version, service_sid=self._solution[
        'service_sid'], asset_sid=self._solution['asset_sid'], sid=sid)