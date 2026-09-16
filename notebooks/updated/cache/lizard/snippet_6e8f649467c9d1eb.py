def delete_webhook(self, id, **data):
    return self.delete('/webhooks/{0}/'.format(id), data=data)