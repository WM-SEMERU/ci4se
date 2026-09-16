def showLayer(self, title='', debugText=''):
    img = PIL.Image.fromarray(self.data, 'RGBA')
    if debugText != '':
        draw = PIL.ImageDraw.Draw(img)
        font = PIL.ImageFont.truetype('DejaVuSansMono.ttf', 24)
        draw.text((0, 0), debugText, (255, 255, 255), font=font)
    img.show(title=title)