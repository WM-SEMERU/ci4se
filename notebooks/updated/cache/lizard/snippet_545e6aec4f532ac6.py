def value(self):
    if (self.mosaicMethod == 'esriMosaicNone' or self.mosaicMethod ==
        'esriMosaicCenter' or self.mosaicMethod == 'esriMosaicNorthwest' or
        self.mosaicMethod == 'esriMosaicNadir'):
        return {'mosaicMethod': 'esriMosaicNone', 'where': self._where,
            'ascending': self._ascending, 'fids': self.fids,
            'mosaicOperation': self._mosaicOperation}
    elif self.mosaicMethod == 'esriMosaicViewpoint':
        return {'mosaicMethod': 'esriMosaicViewpoint', 'viewpoint': self.
            _viewpoint.asDictionary, 'where': self._where, 'ascending':
            self._ascending, 'fids': self._fids, 'mosaicOperation': self.
            _mosaicOperation}
    elif self.mosaicMethod == 'esriMosaicAttribute':
        return {'mosaicMethod': 'esriMosaicAttribute', 'sortField': self.
            _sortField, 'sortValue': self._sortValue, 'ascending': self.
            _ascending, 'where': self._where, 'fids': self._fids,
            'mosaicOperation': self._mosaicOperation}
    elif self.mosaicMethod == 'esriMosaicLockRaster':
        return {'mosaicMethod': 'esriMosaicLockRaster', 'lockRasterIds':
            self._localRasterIds, 'where': self._where, 'ascending': self.
            _ascending, 'fids': self._fids, 'mosaicOperation': self.
            _mosaicOperation}
    elif self.mosaicMethod == 'esriMosaicSeamline':
        return {'mosaicMethod': 'esriMosaicSeamline', 'where': self._where,
            'fids': self._fids, 'mosaicOperation': self._mosaicOperation}
    else:
        raise AttributeError('Invalid Mosaic Method')