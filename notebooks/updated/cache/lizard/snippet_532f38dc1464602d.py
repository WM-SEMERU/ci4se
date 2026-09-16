def getScreenDetails(self):
    primary_screen = None
    screens = []
    for monitor in AppKit.NSScreen.screens():
        screen = {'rect': (int(monitor.frame().origin.x), int(monitor.frame
            ().origin.y), int(monitor.frame().size.width), int(monitor.
            frame().size.height))}
        screens.append(screen)
    return screens