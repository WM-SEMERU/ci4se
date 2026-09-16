def _generate_result(self, callname, result):
    schema = self.api.result_schema()
    schema.context['callname'] = callname
    self.callback(schema.load(result), self.context)