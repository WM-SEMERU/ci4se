def create_parameter_map(self):
    names = self.modelInstance.names
    db = self.modelInstance.database['items']
    parameter_map = {}

    def get_names_index(my_thing):
        return [i for i, x in enumerate(names) if x == my_thing][0]
    for k, this_item in db.items():
        if this_item['type'] == 'process':
            production_id = [x['input'] for x in this_item['exchanges'] if 
                x['type'] == 'production'][0]
            input_ids = [x['input'] for x in this_item['exchanges'] if x[
                'type'] == 'technosphere']
            production_index = get_names_index(db[production_id]['name'])
            input_indexes = [get_names_index(db[x]['name']) for x in input_ids]
            parameter_ids = ['n_p_{}_{}'.format(x, production_index) for x in
                input_indexes]
            parameter_map_items = {(input_ids[n], k): parameter_ids[n] for 
                n, x in enumerate(input_ids)}
            parameter_map.update(parameter_map_items)
    self.parameter_map = parameter_map