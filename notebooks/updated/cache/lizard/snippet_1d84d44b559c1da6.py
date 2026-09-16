def list_rooms(self, message):
    context = {'rooms': self.available_rooms.values()}
    self.say(rendered_template('rooms.html', context), message=message,
        html=True)