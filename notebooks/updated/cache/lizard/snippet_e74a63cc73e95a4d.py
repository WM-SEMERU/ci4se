def receive_trial_result(self, parameter_id, parameters, value):
    logger.debug('acquiring lock for param {}'.format(parameter_id))
    self.thread_lock.acquire()
    logger.debug('lock for current acquired')
    reward = extract_scalar_reward(value)
    if self.optimize_mode is OptimizeMode.Minimize:
        reward = -reward
    logger.debug('receive trial result is:\n')
    logger.debug(str(parameters))
    logger.debug(str(reward))
    indiv = Individual(indiv_id=int(os.path.split(parameters['save_dir'])[1
        ]), graph_cfg=graph_loads(parameters['graph']), result=reward)
    self.population.append(indiv)
    logger.debug('releasing lock')
    self.thread_lock.release()
    self.events[indiv.indiv_id].set()