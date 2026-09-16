def _validate(self):
    if not isinstance(self.box[1], FileTypeBox):
        msg = '{filename} does not contain a valid File Type box.'
        msg = msg.format(filename=self.filename)
        raise IOError(msg)
    ftyp = self.box[1]
    if ftyp.brand == 'jp2 ':
        jp2h = [box for box in self.box if box.box_id == 'jp2h'][0]
        colrs = [box for box in jp2h.box if box.box_id == 'colr']
        for colr in colrs:
            if colr.method not in (core.ENUMERATED_COLORSPACE, core.
                RESTRICTED_ICC_PROFILE):
                msg = (
                    "Color Specification box method must specify either an enumerated colorspace or a restricted ICC profile if the file type box brand is 'jp2 '."
                    )
                warnings.warn(msg, UserWarning)