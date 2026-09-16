def region_screenshot(self, filename=None):
    screen = self.__last_screen if self.__keep_screen else self.screenshot()
    if self.bounds:
        screen = screen.crop(self.bounds)
    if filename:
        screen.save(filename)
    return screen