def get_interims_data(self):
    form = self.request.form
    if 'item_data' not in form:
        return {}
    item_data = {}
    if type(form['item_data']) == list:
        for i_d in form['item_data']:
            for i, d in json.loads(i_d).items():
                item_data[i] = d
        return item_data
    return json.loads(form['item_data'])