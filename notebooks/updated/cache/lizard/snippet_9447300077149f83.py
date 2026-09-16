def set_scf_algorithm_and_iterations(self, algorithm='diis', iterations=50):
    available_algorithms = {'diis', 'dm', 'diis_dm', 'diis_gdm', 'gdm',
        'rca', 'rca_diis', 'roothaan'}
    if algorithm.lower() not in available_algorithms:
        raise ValueError('Algorithm ' + algorithm +
            ' is not available in QChem')
    self.params['rem']['scf_algorithm'] = algorithm.lower()
    self.params['rem']['max_scf_cycles'] = iterations