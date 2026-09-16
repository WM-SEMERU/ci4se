def delete(self, run_id):
    self.generic_dao.delete_record(self.metrics_collection_name, {'run_id':
        self._parse_run_id(run_id)})