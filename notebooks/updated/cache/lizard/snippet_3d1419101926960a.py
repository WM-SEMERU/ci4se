def execute(self, q, args=()):
    self.rowcount = None
    response = None
    if self.query is None:
        self.execute_select(q, args)
    else:
        response = self.execute_django(q, args)
        if isinstance(response, list):
            return
    if response and response.text:
        data = response.json(parse_float=decimal.Decimal)
        if 'totalSize' in data:
            self.rowcount = data['totalSize']
        elif 'success' in data and 'id' in data:
            self.lastrowid = data['id']
            return
        elif 'compositeResponse' in data:
            self.lastrowid = [(x['body']['id'] if x['body'] is not None else
                x['referenceId']) for x in data['compositeResponse']]
            return
        elif data['hasErrors'] is False:
            if data['results'] and data['results'][0]['result']:
                self.lastrowid = [item['result']['id'] for item in data[
                    'results']]
            return
        else:
            raise DatabaseError(data)
        if not q.upper().startswith('SELECT COUNT() FROM'):
            self.first_row = data['records'][0] if data['records'] else None