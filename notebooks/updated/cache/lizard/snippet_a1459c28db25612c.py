def countApproxDistinct(self, relativeSD=0.05):
    if relativeSD < 1.7e-05:
        raise ValueError('relativeSD should be greater than 0.000017')
    hashRDD = self.map(lambda x: portable_hash(x) & 4294967295)
    return hashRDD._to_java_object_rdd().countApproxDistinct(relativeSD)