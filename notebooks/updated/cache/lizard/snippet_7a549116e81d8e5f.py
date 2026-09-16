def summon(self, card):
    if isinstance(card, str):
        card = self.card(card, zone=Zone.PLAY)
    self.game.cheat_action(self, [Summon(self, card)])
    return card