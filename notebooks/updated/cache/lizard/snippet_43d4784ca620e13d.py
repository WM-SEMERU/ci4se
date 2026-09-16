def update_positions(self):
    user_list = []
    for key in self.positions.keys():
        user_list.append(key)
    if not user_list:
        return self.positions
    import requests
    url = self.endpoint + '/location'
    while user_list:
        if len(user_list) > 50:
            user_batch = user_list[0:50]
        else:
            user_batch = user_list
        params = {'group': self.group_name, 'users': ','.join(user_batch),
            'n': 1}
        response = requests.get(url, params=params)
        response_details = response.json()
        from labpack.records.time import labDT
        if 'users' in response_details.keys():
            for key in response_details['users'].keys():
                position_details = {}
                if key in user_batch:
                    for entry in response_details['users'][key]:
                        if 'time' in entry.keys() and 'location' in entry.keys(
                            ):
                            time_string = entry['time']
                            time_string = time_string.replace(' +0000 UTC', 'Z'
                                )
                            time_string = time_string.replace(' ', 'T')
                            time_dt = labDT.fromISO(time_string).epoch()
                            position_details = {'time': time_dt, 'location':
                                entry['location']}
                            break
                    self.positions[key] = position_details
        if len(user_list) > 50:
            user_list = user_list[50:0]
        else:
            user_list = []
    return self.positions