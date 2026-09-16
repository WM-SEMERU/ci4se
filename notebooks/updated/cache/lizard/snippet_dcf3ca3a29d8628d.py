def card_names_and_ids(self):
    b = Board(self.client, self.board_id)
    cards = b.getCards()
    card_names_and_ids = [(unidecode(c.name), c.id) for c in cards]
    return card_names_and_ids