def get_datastrip_list(self):
    datastrips = self.product_info['datastrips']
    return [(self.get_datastrip_name(datastrip['id']), self.base_url +
        datastrip['path']) for datastrip in datastrips]