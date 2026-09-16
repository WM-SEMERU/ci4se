def stratify_s(self):
    pscore_order = self.raw_data['pscore'].argsort()
    pscore = self.raw_data['pscore'][pscore_order]
    D = self.raw_data['D'][pscore_order]
    logodds = np.log(pscore / (1 - pscore))
    K = self.raw_data['K']
    blocks_uniq = set(select_blocks(pscore, logodds, D, K, 0, 1))
    self.blocks = sorted(blocks_uniq)
    self.stratify()