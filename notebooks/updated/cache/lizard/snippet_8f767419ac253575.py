def osCopy(self):
    k = Keyboard()
    k.keyDown('{CTRL}')
    k.type('c')
    k.keyUp('{CTRL}')