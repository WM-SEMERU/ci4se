def use_plenary_resource_view(self):
    self._object_views['resource'] = PLENARY
    for session in self._get_provider_sessions():
        try:
            session.use_plenary_resource_view()
        except AttributeError:
            pass