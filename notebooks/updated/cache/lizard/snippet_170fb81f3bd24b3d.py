def mongo_to_object(self, statement_data):
    Statement = self.get_model('statement')
    statement_data['id'] = statement_data['_id']
    return Statement(**statement_data)