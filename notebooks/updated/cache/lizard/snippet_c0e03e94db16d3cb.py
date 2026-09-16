def get_config(self, retrieve='all'):
    get_startup = retrieve == 'all' or retrieve == 'startup'
    get_running = retrieve == 'all' or retrieve == 'running'
    get_candidate = retrieve == 'all' or retrieve == 'candidate'
    if retrieve == 'all' or get_running:
        result = self._execute_command_with_vdom('show')
        text_result = '\n'.join(result)
        return {'startup': '', 'running': py23_compat.text_type(text_result
            ), 'candidate': ''}
    elif get_startup or get_candidate:
        return {'startup': '', 'running': '', 'candidate': ''}