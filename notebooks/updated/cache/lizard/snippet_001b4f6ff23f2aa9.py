def set_desktop_wallpaper(desktop, img):
    desktop = str(desktop).lower()
    if 'xfce' in desktop or 'xubuntu' in desktop:
        xfconf('/backdrop/screen0/monitor0/image-path', img)
        xfconf('/backdrop/screen0/monitor0/workspace0/last-image', img)
    elif 'muffin' in desktop or 'cinnamon' in desktop:
        util.disown(['gsettings', 'set', 'org.cinnamon.desktop.background',
            'picture-uri', 'file://' + urllib.parse.quote(img)])
    elif 'gnome' in desktop or 'unity' in desktop:
        util.disown(['gsettings', 'set', 'org.gnome.desktop.background',
            'picture-uri', 'file://' + urllib.parse.quote(img)])
    elif 'mate' in desktop:
        util.disown(['gsettings', 'set', 'org.mate.background',
            'picture-filename', img])
    elif 'sway' in desktop:
        util.disown(['swaymsg', 'output', '*', 'bg', img, 'fill'])
    elif 'awesome' in desktop:
        util.disown(['awesome-client',
            "require('gears').wallpaper.maximized('{img}')".format(**locals())]
            )
    else:
        set_wm_wallpaper(img)