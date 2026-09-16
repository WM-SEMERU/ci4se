def user_list(self, name=None, name_matches=None, min_level=None, max_level
    =None, level=None, user_id=None, order=None):
    params = {'search[name]': name, 'search[name_matches]': name_matches,
        'search[min_level]': min_level, 'search[max_level]': max_level,
        'search[level]': level, 'search[id]': user_id, 'search[order]': order}
    return self._get('users.json', params)