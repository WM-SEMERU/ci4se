def mine(tgt=None, tgt_type='glob', **kwargs):
    pillar_util = salt.utils.master.MasterPillarUtil(tgt, tgt_type,
        use_cached_grains=False, grains_fallback=False, use_cached_pillar=
        False, pillar_fallback=False, opts=__opts__)
    cached_mine = pillar_util.get_cached_mine_data()
    return cached_mine