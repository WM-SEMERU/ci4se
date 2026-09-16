def use_plenary_gradebook_view(self):
    self._gradebook_view = PLENARY
    for session in self._get_provider_sessions():
        try:
            session.use_plenary_gradebook_view()
        except AttributeError:
            pass