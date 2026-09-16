def proximal(self):
    return proximal_convex_conj(proximal_convex_conj_kl(space=self.domain,
        g=self.prior))