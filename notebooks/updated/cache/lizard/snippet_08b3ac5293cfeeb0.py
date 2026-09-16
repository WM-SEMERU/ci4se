def convert_rect(self, rect):
    return Container.convert_rect(self, rect).move(-self.offset)