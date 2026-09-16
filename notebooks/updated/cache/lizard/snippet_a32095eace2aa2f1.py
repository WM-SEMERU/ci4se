def send_letter(self, file_list, destination='DE', duplex=True, color=False,
    user_transaction=None, gogreen=False, test_environment=False):
    idx = 0
    last = len(file_list) - 1
    multiple_files = True if len(file_list) > 1 else False
    letter_id = None
    for file in file_list:
        files = {'file': file}
        if idx == 0:
            data = {'settings[destination]': destination,
                'settings[simplex]': 'NONE' if duplex else 'ALL',
                'settings[color]': 'ALL' if color else 'NONE',
                'settings[user_transaction]': user_transaction,
                'settings[test_environment]': test_environment,
                'settings[gogreen]': True if gogreen else False,
                'incomplete': True if multiple_files else False}
            send_req = self._make_post_request('letters', data=data, files=
                files)
            if send_req:
                if not multiple_files:
                    return json.loads(send_req)['id']
                else:
                    letter_id = json.loads(send_req)['id']
            else:
                return send_req
        if idx > 0:
            if idx == last:
                self._make_patch_request('letters/{}'.format(letter_id),
                    data={'incomplete': False}, files=files)
            else:
                self._make_patch_request('letters/{}'.format(letter_id),
                    data={'incomplete': True}, files=files)
        idx += 1
    return letter_id