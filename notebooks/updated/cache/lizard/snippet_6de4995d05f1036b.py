def draw(self, img, pixmapper, bounds):
    if self.hidden:
        return
    if self.trail is not None:
        self.trail.draw(img, pixmapper, bounds)
    icon = self.img()
    px, py = pixmapper(self.latlon)
    px -= icon.width / 2
    py -= icon.height / 2
    w = icon.width
    h = icon.height
    px, py, sx, sy, w, h = self.clip(px, py, w, h, img)
    cv.SetImageROI(icon, (sx, sy, w, h))
    cv.SetImageROI(img, (px, py, w, h))
    cv.Add(icon, img, img)
    cv.ResetImageROI(img)
    cv.ResetImageROI(icon)
    self.posx = px + w / 2
    self.posy = py + h / 2