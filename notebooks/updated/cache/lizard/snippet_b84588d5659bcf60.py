def step(self):
    self.director.window.switch_to()
    self.director.window.dispatch_events()
    self.director.window.dispatch_event('on_draw')
    self.director.window.flip()
    pyglet.clock.tick()