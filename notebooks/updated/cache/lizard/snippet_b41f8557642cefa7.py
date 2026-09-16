def inverse_transform(self, Xs=None, ys=None, Xt=None, yt=None, batch_size=128
    ):
    if check_params(Xt=Xt):
        transp_Xt = Xt.dot(self.A1_) + self.B1_
        return transp_Xt