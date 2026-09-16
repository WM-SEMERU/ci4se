def get_result(self):
    result = get_json_from_remote_server(self.call)
    if result:
        date, value = max(result.iteritems(), key=itemgetter(1))
        return {'date': date, 'users': value}
    else:
        return {'date': 'No Data', 'users': 0}