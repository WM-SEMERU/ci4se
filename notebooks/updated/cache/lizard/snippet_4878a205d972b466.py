def uninvert_unique_two_lists(flat_list, reconstruct_tup):
    import utool as ut
    inverse3, cumsum, inverse2, inverse1 = reconstruct_tup
    flat_stacked_ = ut.take(flat_list, inverse3)
    unique_list1_, unique_list2_ = ut.unflatten2(flat_stacked_, cumsum)
    res_list1_ = ut.take(unique_list1_, inverse1)
    res_list2_ = ut.take(unique_list2_, inverse2)
    return res_list1_, res_list2_