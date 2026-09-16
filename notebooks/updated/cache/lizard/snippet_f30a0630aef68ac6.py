def image_entropy(im):
    if not isinstance(im, Image.Image):
        return 0
    hist = im.histogram()
    hist_size = float(sum(hist))
    hist = [(h / hist_size) for h in hist]
    return -sum([(p * math.log(p, 2)) for p in hist if p != 0])