def loc(self):
    try:
        return '{}:{}'.format(*ParseError.loc_info(self.text, self.index))
    except ValueError:
        return '<out of bounds index {!r}>'.format(self.index)