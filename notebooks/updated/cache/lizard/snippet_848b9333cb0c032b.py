def get_serializable_dict(self):
    tmp = self.get_dict()
    tmp['date_download'] = str(tmp['date_download'])
    tmp['date_modify'] = str(tmp['date_modify'])
    tmp['date_publish'] = str(tmp['date_publish'])
    return tmp