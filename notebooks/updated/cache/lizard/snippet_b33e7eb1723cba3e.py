def use_comparative_asset_view(self):
    self._object_views['asset'] = COMPARATIVE
    for session in self._get_provider_sessions():
        try:
            session.use_comparative_asset_view()
        except AttributeError:
            pass