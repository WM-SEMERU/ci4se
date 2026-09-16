def get_proficiencies_by_search(self, proficiency_query, proficiency_search):
    if not self._can('search'):
        raise PermissionDenied()
    return self._provider_session.get_proficiencies_by_search(proficiency_query
        , proficiency_search)