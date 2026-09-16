def intervalCreateSimulateAnalyze(netParams=None, simConfig=None, output=
    False, interval=None):
    import os
    from .. import sim
    pops, cells, conns, stims, rxd, simData = sim.create(netParams,
        simConfig, output=True)
    try:
        if sim.rank == 0:
            if os.path.exists('temp'):
                for f in os.listdir('temp'):
                    os.unlink('temp/{}'.format(f))
            else:
                os.mkdir('temp')
        sim.intervalSimulate(interval)
    except Exception as e:
        print(e)
        return
    sim.pc.barrier()
    sim.analyze()
    if output:
        return pops, cells, conns, stims, simData