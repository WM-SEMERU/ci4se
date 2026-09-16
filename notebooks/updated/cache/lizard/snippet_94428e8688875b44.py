def _write_mosaic(self, key, outfile):
    maxsize = self.settings.get('max_mosaic_size', 100000000.0)
    channel = self.fv.get_channel(self.chname)
    image = channel.datasrc[key]
    if image.width * image.height > maxsize:
        s = 'Mosaic too large to be written {0}'.format(image.shape)
        self.w.status.set_text(s)
        self.logger.error(s)
        return
    hdu = fits.PrimaryHDU(image.get_data())
    self._write_header(image, hdu)
    self._write_history(key, hdu)
    if minversion(astropy, '1.3'):
        hdu.writeto(outfile, overwrite=True)
    else:
        hdu.writeto(outfile, clobber=True)