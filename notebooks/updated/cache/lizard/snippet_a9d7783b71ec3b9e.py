def add_item(self, item_url, item_metadata):
    c = self.conn.cursor()
    c.execute('DELETE FROM items WHERE url=?', (str(item_url),))
    self.conn.commit()
    c.execute('INSERT INTO items VALUES (?, ?, ?)', (str(item_url),
        item_metadata, self.__now_iso_8601()))
    self.conn.commit()
    c.close()