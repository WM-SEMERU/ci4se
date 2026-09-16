def users(self):
    existing_users = self.existing_users()
    existing_user_ids = [x['id'] for x in existing_users]
    sharing = getMultiAdapter((self.my_workspace(), self.request), name=
        'sharing')
    search_results = sharing.user_search_results()
    users = existing_users + [x for x in search_results if x['id'] not in
        existing_user_ids]
    users.sort(key=lambda x: safe_unicode(x['title']))
    return users