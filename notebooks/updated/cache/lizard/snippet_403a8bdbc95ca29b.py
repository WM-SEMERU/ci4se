def gmf_data_dt(self):
    return numpy.dtype([('rlzi', U16), ('sid', U32), ('eid', U64), ('gmv',
        (F32, (len(self.imtls),)))])