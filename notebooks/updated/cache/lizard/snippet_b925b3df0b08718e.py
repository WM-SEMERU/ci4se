def get_activities_by_search(self, activity_query, activitiesearch):
    if not self._can('search'):
        raise PermissionDenied()
    return self._provider_session.get_activities_by_search(activity_query,
        activitiesearch)