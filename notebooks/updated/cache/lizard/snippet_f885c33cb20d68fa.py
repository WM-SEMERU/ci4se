def CopyToDict(self):
    result_dict = {'labels': self.labels}
    if self.comment:
        result_dict['comment'] = self.comment
    return result_dict