def analyze(self, scratch, **kwargs):
    changes = dict((x.name, self.sprite_changes(x)) for x in scratch.sprites)
    changes['stage'] = {'background': self.attribute_state(scratch.stage.
        scripts, 'costume')}
    return {'initialized': changes}