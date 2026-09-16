def build(self, title, text, img_url):
    super(ImageCard, self).build()
    self.title = Title(id=self.id + '-title', text=title, classname=
        'card-title', size=3, parent=self)
    self.block = Panel(id=self.id + '-block', classname='card-block',
        parent=self)
    self.image = Image(id=self.id + '-image', img_url=img_url, classname=
        'card-image-top img-fluid', parent=self.block)
    self.text = Paragraph(id=self.id + '-text', text=text, classname=
        'card-text', parent=self.block)