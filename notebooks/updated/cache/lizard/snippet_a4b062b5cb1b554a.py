def _init_table_from_dfa(self, mma):
    observation_table_init = ObservationTableInit(self.epsilon, self.alphabet)
    sm_vector, smi_vector, em_vector = observation_table_init.initialize(mma,
        True)
    self.observation_table.sm_vector = sm_vector
    self.observation_table.smi_vector = smi_vector
    self.observation_table.em_vector = em_vector
    logging.info('Initialized from DFA em_vector table is the following:')
    logging.info(em_vector)
    self._fill_table_entry(self.epsilon, self.epsilon)
    for row in sorted(list(set(sm_vector + smi_vector)), key=len)[1:]:
        for column in em_vector:
            self._fill_table_entry(str(row), str(column))