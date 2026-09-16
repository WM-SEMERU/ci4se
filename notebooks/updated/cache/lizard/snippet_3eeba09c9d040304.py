def farthest(self, dt1, dt2, *dts):
    from functools import reduce
    dt1 = pendulum.instance(dt1)
    dt2 = pendulum.instance(dt2)
    dts = [dt1, dt2] + [pendulum.instance(x) for x in dts]
    dts = [(abs(self - dt), dt) for dt in dts]
    return max(dts)[1]