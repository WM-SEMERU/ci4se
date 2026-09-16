def all_mouse_sprites(self):

    def all_recursive(sprites):
        if not sprites:
            return
        for sprite in sprites:
            if sprite.visible:
                yield sprite
                for child in all_recursive(sprite.get_mouse_sprites()):
                    yield child
    return all_recursive(self.get_mouse_sprites())