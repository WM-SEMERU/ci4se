def get_store_local_final_result(self):
    fw_dict = self.get_fw_dict()
    fw_data, fw_data_dict = self.get_fw(fw_dict.get('fw_id'))
    res = fw_data.result
    self.store_local_final_result(res)