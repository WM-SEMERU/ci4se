def _initLayerCtors(self):
    ctors = {'lmdb': s_lmdblayer.LmdbLayer, 'remote': s_remotelayer.RemoteLayer
        }
    self.layrctors.update(**ctors)