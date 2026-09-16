def devid(self):
    d = self.device
    vend_id = d.get('ID_VENDOR_ID')
    model_id = d.get('ID_MODEL_ID')
    return vend_id, model_id