def rotate_about(self, p, theta):
    result = self.clone()
    result.translate(-p.x, -p.y)
    result.rotate(theta)
    result.translate(p.x, p.y)
    return result