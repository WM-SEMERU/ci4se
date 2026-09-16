def collectInterest(self):
    if self.collectedInterest:
        return False
    pg = self.usr.getPage('http://www.neopets.com/bank.phtml')
    form = pg.form(action='process_bank.phtml')
    form['type'] = 'interest'
    pg = form.submit()
    if "It's great to see you again" in pg.content:
        self.__loadDetails(pg)
        return True
    else:
        logging.getLogger('neolib.user').info(
            'Failed to collect daily interest for unknown reason.', {'pg': pg})
        return False