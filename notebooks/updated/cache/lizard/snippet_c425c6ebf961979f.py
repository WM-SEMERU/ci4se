def makeicons(source):
    im = Image.open(source)
    for name, (_, w, h, func) in icon_sizes.iteritems():
        print('Making icon %s...' % name)
        tn = func(im, (w, h))
        bg = Image.new('RGBA', (w, h), (255, 255, 255))
        x = w / 2 - tn.size[0] / 2
        y = h / 2 - tn.size[1] / 2
        bg.paste(tn, (x, y))
        bg.save(path.join(env.dir, name))