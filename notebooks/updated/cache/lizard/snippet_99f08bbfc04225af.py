def on_portal(self, *args):
    if not (self.board and self.origin and self.destination and self.origin
        .name in self.board.character.portal and self.destination.name in
        self.board.character.portal):
        Clock.schedule_once(self.on_portal, 0)
        return
    self.name = '{}->{}'.format(self.portal['origin'], self.portal[
        'destination'])