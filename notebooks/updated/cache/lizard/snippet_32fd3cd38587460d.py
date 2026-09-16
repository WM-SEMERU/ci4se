def _param_callback(self, name, value):
    print('{0}: {1}'.format(name, value))
    self._param_check_list.remove(name)
    if len(self._param_check_list) == 0:
        print('Have fetched all parameter values.')
        for g in self._param_groups:
            self._cf.param.remove_update_callback(group=g, cb=self.
                _param_callback)
        pkd = random.random()
        print('')
        print('Write: pid_attitude.pitch_kd={:.2f}'.format(pkd))
        self._cf.param.add_update_callback(group='pid_attitude', name=
            'pitch_kd', cb=self._a_pitch_kd_callback)
        self._cf.param.set_value('pid_attitude.pitch_kd', '{:.2f}'.format(pkd))