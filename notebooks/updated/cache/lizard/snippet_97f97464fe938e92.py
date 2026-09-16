def tile(self, z, x, y):
    logger.debug(_('Render tile %s') % ((z, x, y),))
    proj = GoogleProjection(self.tilesize, [z])
    return self.render(proj.tile_bbox((z, x, y)))