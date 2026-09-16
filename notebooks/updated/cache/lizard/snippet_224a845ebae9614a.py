def perform_action(self, action, machines, params, progress_title,
    success_title):
    if len(machines) == 0:
        return 0
    with utils.Spinner() as context:
        return self._async_perform_action(context, action, list(machines),
            params, progress_title, success_title)