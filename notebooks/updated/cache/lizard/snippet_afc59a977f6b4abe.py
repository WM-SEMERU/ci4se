def create(netParams=None, simConfig=None, output=False):
    from .. import sim
    import __main__ as top
    if not netParams:
        netParams = top.netParams
    if not simConfig:
        simConfig = top.simConfig
    sim.initialize(netParams, simConfig)
    pops = sim.net.createPops()
    cells = sim.net.createCells()
    conns = sim.net.connectCells()
    stims = sim.net.addStims()
    rxd = sim.net.addRxD()
    simData = sim.setupRecording()
    if output:
        return pops, cells, conns, rxd, stims, simData