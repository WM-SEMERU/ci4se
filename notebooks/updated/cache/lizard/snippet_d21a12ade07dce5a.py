def initialize_page_data(self):
    if self.term.is_a_tty:
        self.display_initialize()
    self.character_generator = self.character_factory(self.screen.wide)
    page_data = list()
    while True:
        try:
            page_data.append(next(self.character_generator))
        except StopIteration:
            break
    if LIMIT_UCS == 65536:
        echo(self.term.center('press any key.').rstrip())
        flushout()
        self.term.inkey(timeout=None)
    return page_data