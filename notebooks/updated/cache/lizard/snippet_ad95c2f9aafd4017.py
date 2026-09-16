def serialisasi(self):
    return {'nama': self.nama, 'nomor': self.nomor, 'kata_dasar': self.
        kata_dasar, 'pelafalan': self.pelafalan, 'bentuk_tidak_baku': self.
        bentuk_tidak_baku, 'varian': self.varian, 'makna': [makna.
        serialisasi() for makna in self.makna]}