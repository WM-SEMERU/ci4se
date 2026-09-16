def makeEndOfPrdvFuncCond(self):
    VLvlNext = self.PermShkVals_temp ** (1.0 - self.CRRA
        ) * self.PermGroFac ** (1.0 - self.CRRA) * self.vFuncNext(self.mNrmNext
        )
    EndOfPrdv_cond = self.DiscFacEff * np.sum(VLvlNext * self.ShkPrbs_temp,
        axis=0)
    EndOfPrdvNvrs_cond = self.uinv(EndOfPrdv_cond)
    EndOfPrdvNvrsP_cond = self.EndOfPrdvP_cond * self.uinvP(EndOfPrdv_cond)
    EndOfPrdvNvrs_cond = np.insert(EndOfPrdvNvrs_cond, 0, 0.0)
    EndOfPrdvNvrsP_cond = np.insert(EndOfPrdvNvrsP_cond, 0,
        EndOfPrdvNvrsP_cond[0])
    aNrm_temp = np.insert(self.aNrm_cond, 0, self.BoroCnstNat)
    EndOfPrdvNvrsFunc_cond = CubicInterp(aNrm_temp, EndOfPrdvNvrs_cond,
        EndOfPrdvNvrsP_cond)
    EndofPrdvFunc_cond = ValueFunc(EndOfPrdvNvrsFunc_cond, self.CRRA)
    return EndofPrdvFunc_cond