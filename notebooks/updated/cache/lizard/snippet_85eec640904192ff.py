def response_data_to_model_instance(self, response_data):
    response_data['datetime_created'] = dateutil.parser.parse(response_data
        ['datetime_created'])
    if response_data['datetime_finished']:
        response_data['datetime_finished'] = dateutil.parser.parse(
            response_data['datetime_finished'])
    return super(BaseTaskInstanceManager, self
        ).response_data_to_model_instance(response_data)