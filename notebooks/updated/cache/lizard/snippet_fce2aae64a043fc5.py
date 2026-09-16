def remove(self):
    Customer.objects.filter(default_source=self.id).update(default_source=None)
    try:
        self._api_delete()
    except InvalidRequestError as exc:
        if 'No such source:' in str(exc) or 'No such customer:' in str(exc):
            pass
        else:
            raise
    self.delete()