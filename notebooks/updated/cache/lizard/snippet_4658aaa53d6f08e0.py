def click(self, x, y, button, press):
    if button == 1:
        if press:
            print(self.fibo.next())
    else:
        self.stop()