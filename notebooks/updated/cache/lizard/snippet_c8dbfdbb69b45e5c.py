def addToStableArmPoints(solution_next, DiscFac, Rfree, CRRA, PermGroFacCmp,
    UnempPrb, PFMPC, Rnrm, Beth, mLowerBnd, mUpperBnd):
    mNrm_list = copy(solution_next.mNrm_list)
    cNrm_list = copy(solution_next.cNrm_list)
    MPC_list = copy(solution_next.MPC_list)
    mNext = mNrm_list[-1]
    if mNext < mUpperBnd:
        cNext = solution_next.cNrm_list[-1]
        MPCNext = solution_next.MPC_list[-1]
        mNow, cNow, MPCnow = findNextPoint(DiscFac, Rfree, CRRA,
            PermGroFacCmp, UnempPrb, Rnrm, Beth, cNext, mNext, MPCNext, PFMPC)
        mNrm_list.append(mNow)
        cNrm_list.append(cNow)
        MPC_list.append(MPCnow)
    mNext = mNrm_list[0]
    if mNext > mLowerBnd:
        cNext = solution_next.cNrm_list[0]
        MPCNext = solution_next.MPC_list[0]
        mNow, cNow, MPCnow = findNextPoint(DiscFac, Rfree, CRRA,
            PermGroFacCmp, UnempPrb, Rnrm, Beth, cNext, mNext, MPCNext, PFMPC)
        mNrm_list.insert(0, mNow)
        cNrm_list.insert(0, cNow)
        MPC_list.insert(0, MPCnow)
    solution_now = TractableConsumerSolution(mNrm_list=mNrm_list, cNrm_list
        =cNrm_list, MPC_list=MPC_list)
    solution_now.PointCount = len(mNrm_list)
    return solution_now