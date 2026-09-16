def process_input(self, character):
    func = None
    try:
        func = getattr(self, 'handle_%s' % chr(character), None)
    except:
        pass
    if func:
        func()