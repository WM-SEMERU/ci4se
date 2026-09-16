def vm_result_update(self, payload):
    port_id = payload.get('port_id')
    result = payload.get('result')
    if port_id and result:
        params = dict(columns=dict(result=result))
        self.update_vm_db(port_id, **params)