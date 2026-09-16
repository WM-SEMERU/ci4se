def create_child_folder(self, folder_name):
    headers = self.headers
    endpoint = ('https://outlook.office.com/api/v2.0/me/MailFolders/' +
        self.id + '/childfolders')
    payload = '{ "DisplayName": "' + folder_name + '"}'
    r = requests.post(endpoint, headers=headers, data=payload)
    if check_response(r):
        return_folder = r.json()
        return self._json_to_folder(self.account, return_folder)