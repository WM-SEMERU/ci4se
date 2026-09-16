def _get_image_entropy(self, image):
    hist = image.histogram()
    hist_size = sum(hist)
    hist = [(float(h) / hist_size) for h in hist]
    return -sum([(p * math.log(p, 2)) for p in hist if p != 0])