def use_comparative_asset_composition_view(self):
    self._object_views['asset_composition'] = COMPARATIVE
    for session in self._get_provider_sessions():
        try:
            session.use_comparative_asset_composition_view()
        except AttributeError:
            pass