def on_join(self, connection, event):
    nickname = self.get_nickname(event)
    nickname_color = color(nickname)
    self.nicknames[nickname] = nickname_color
    self.namespace.emit('join')
    self.namespace.emit('message', nickname, 'joins', nickname_color)
    self.emit_nicknames()