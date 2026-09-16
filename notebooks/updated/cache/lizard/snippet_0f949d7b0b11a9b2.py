def lines(self, lines_dict, y='bottom', color='grey', **kwargs):
    for l, x in lines_dict.items():
        self.line(x, l, y, color, **kwargs)