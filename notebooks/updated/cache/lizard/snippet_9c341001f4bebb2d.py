def clear(self, asset_manager_id, book_ids=None):
    self.logger.info('Clear Transactions & Positions - Asset Manager: %s',
        asset_manager_id)
    url = '%s/clear/%s' % (self.endpoint, asset_manager_id)
    params = {'asset_manager_ids': ','.join(book_ids)} if book_ids else {}
    response = self.session.delete(url, params=params)
    if response.ok:
        tran_count = response.json().get('transaction_count', 'Unknown')
        self.logger.info('Deleted %s Transactions.', tran_count)
        pos_count = response.json().get('position_count', 'Unknown')
        self.logger.info('Deleted %s Positions.', pos_count)
        return response.json()
    else:
        self.logger.error(response.text)
        response.raise_for_status()