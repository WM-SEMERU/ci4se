def via_clb_upi(self, clb_upi, det_id):
    try:
        return DOM.from_json([d for d in self._json if d['CLBUPI'] ==
            clb_upi and d['DetOID'] == det_id][0])
    except IndexError:
        log.critical("No DOM found for CLB UPI '{0}'".format(clb_upi))