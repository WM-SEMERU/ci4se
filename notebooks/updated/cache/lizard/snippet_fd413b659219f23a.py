async def act(self):
    self.age += 1
    self.added_last = False
    self.learn_from_domain(method=self.env_learning_method, amount=self.
        env_learning_amount)
    artifact = self.invent(self.search_width)
    args = artifact.framings[self.name]['args']
    val = artifact.evals[self.name]
    self._log(logging.DEBUG, 'Created spirograph with args={}, val={}'.
        format(args, val))
    self.spiro_args = args
    self.arg_history.append(self.spiro_args)
    self.add_artifact(artifact)
    if val >= self._own_threshold:
        artifact.self_criticism = 'pass'
        self.learn(artifact, self.teaching_iterations)
        self.add_candidate(artifact)
        self.added_last = True
    elif self.jump == 'random':
        largs = self.spiro_args
        self.spiro_args = np.random.uniform(-199, 199, self.spiro_args.shape)
        self._log(logging.DEBUG, 'Jumped from {} to {}'.format(largs, self.
            spiro_args))
    self.save_images(artifact)