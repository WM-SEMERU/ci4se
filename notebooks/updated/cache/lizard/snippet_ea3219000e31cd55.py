def set_params(self, **params):
    if 'precomputed' in params and params['precomputed'] != self.precomputed:
        raise ValueError('Cannot update precomputed. Please create a new graph'
            )
    if 'distance' in params and params['distance'
        ] != self.distance and self.precomputed is None:
        raise ValueError('Cannot update distance. Please create a new graph')
    if 'knn' in params and params['knn'
        ] != self.knn and self.precomputed is None:
        raise ValueError('Cannot update knn. Please create a new graph')
    if 'decay' in params and params['decay'
        ] != self.decay and self.precomputed is None:
        raise ValueError('Cannot update decay. Please create a new graph')
    if 'bandwidth' in params and params['bandwidth'
        ] != self.bandwidth and self.precomputed is None:
        raise ValueError('Cannot update bandwidth. Please create a new graph')
    if 'bandwidth_scale' in params and params['bandwidth_scale'
        ] != self.bandwidth_scale:
        raise ValueError(
            'Cannot update bandwidth_scale. Please create a new graph')
    super().set_params(**params)
    return self