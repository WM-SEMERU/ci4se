def create_request(self):
    fis_service = FisService(instance_id=self.instance_id)
    self.download_list = fis_service.get_request(self)