def update(self):
    for x in range(1, self.inventory.pages + 1):
        if self._hasPageChanged(x):
            form = self._updateForm(x)
            form.usePin = True
            pg = form.submit()
            if 'Your Safety Deposit Box' in pg.content:
                return True
            else:
                logging.getLogger('neolib.shop').exception(
                    'Could not verify if SDB inventory was updated.', {'pg':
                    pg})
                return False