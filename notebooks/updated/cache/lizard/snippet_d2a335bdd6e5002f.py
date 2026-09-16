def get_ec(self, ec_handle):
    with self._mutex:
        for ec in self.owned_ecs:
            if ec.handle == ec_handle:
                return ec
        for ec in self.participating_ecs:
            if ec.handle == ec_handle:
                return ec
        raise exceptions.NoECWithHandleError