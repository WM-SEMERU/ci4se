def attach_many(self, *medias: typing.Union[InputMedia, typing.Dict]):
    for media in medias:
        self.attach(media)