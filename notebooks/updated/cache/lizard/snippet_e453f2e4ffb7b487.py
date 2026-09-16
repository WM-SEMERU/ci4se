def delete_object(self, id):
    return self.request('{0}/{1}'.format(self.version, id), method='DELETE')