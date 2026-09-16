def encode2(self):
    buf = BytesIO()
    self.fig.savefig(buf, format='png', bbox_inches='tight', dpi=100)
    buf.seek(0)
    string = b64encode(buf.read())
    return '<img src="data:image/png;base64,{0}">'.format(urlquote(string))