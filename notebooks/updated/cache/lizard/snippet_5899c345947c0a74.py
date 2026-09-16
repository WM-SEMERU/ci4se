def overlaps(self, canvas, exclude=[]):
    try:
        exclude = list(exclude)
    except TypeError:
        exclude = [exclude]
    exclude.append(self)
    for selfY, row in enumerate(self.image.image()):
        for selfX, pixel in enumerate(row):
            canvasPixelOn = canvas.testPixel((selfX + self.position[0], 
                selfY + self.position[1]), excludedSprites=exclude)
            if pixel and canvasPixelOn:
                return True
    return False