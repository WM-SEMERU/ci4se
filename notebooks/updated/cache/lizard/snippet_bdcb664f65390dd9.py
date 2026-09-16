def save(self, fname):
    element = _transform.SVGFigure(self.width, self.height)
    element.append(self)
    element.save(os.path.join(CONFIG['figure.save_path'], fname))