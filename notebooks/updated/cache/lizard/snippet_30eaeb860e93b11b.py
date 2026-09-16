def scroll_window(self, lines):
    u
    top = self.WindowTop + lines
    if top < 0:
        top = 0
    if top + System.Console.WindowHeight > System.Console.BufferHeight:
        top = System.Console.BufferHeight
    self.WindowTop = top