def pvwatts_losses(soiling=2, shading=3, snow=0, mismatch=2, wiring=2,
    connections=0.5, lid=1.5, nameplate_rating=1, age=0, availability=3):
    r
    params = [soiling, shading, snow, mismatch, wiring, connections, lid,
        nameplate_rating, age, availability]
    perf = 1
    for param in params:
        perf *= 1 - param / 100
    losses = (1 - perf) * 100.0
    return losses