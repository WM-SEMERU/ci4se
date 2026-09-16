def generate_trajs(self, M, N, start=None, stop=None, dt=1):
    from msmtools.generation import generate_trajs
    return generate_trajs(self._P, M, N, start=start, stop=stop, dt=dt)