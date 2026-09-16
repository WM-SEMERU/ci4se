def train(self, true_sampler, generative_model, discriminative_model,
    iter_n=100, k_step=10):
    if isinstance(true_sampler, TrueSampler) is False:
        raise TypeError('The type of `true_sampler` must be `TrueSampler`.')
    if isinstance(generative_model, AutoEncoderModel) is False:
        raise TypeError(
            'The type of `generative_model` must be `AutoEncoderModel`.')
    if isinstance(discriminative_model, DiscriminativeModel) is False:
        raise TypeError(
            'The type of `discriminative_model` must be `DiscriminativeModel`.'
            )
    a_logs_list = []
    d_logs_list = []
    g_logs_list = []
    try:
        for n in range(iter_n):
            self.__logger.debug('-' * 100)
            self.__logger.debug('Iterations: (' + str(n + 1) + '/' + str(
                iter_n) + ')')
            self.__logger.debug('-' * 100)
            self.__logger.debug("The `auto_encoder`'s turn.")
            self.__logger.debug('-' * 100)
            generative_model, a_logs_list = self.train_auto_encoder(
                generative_model, a_logs_list)
            self.__logger.debug('-' * 100)
            self.__logger.debug("The `discriminator`'s turn.")
            self.__logger.debug('-' * 100)
            discriminative_model, d_logs_list = self.train_discriminator(k_step
                , true_sampler, generative_model, discriminative_model,
                d_logs_list)
            self.__logger.debug('-' * 100)
            self.__logger.debug("The `generator`'s turn.")
            self.__logger.debug('-' * 100)
            generative_model, g_logs_list = self.train_generator(
                generative_model, discriminative_model, g_logs_list)
    except KeyboardInterrupt:
        print('Keyboard Interrupt.')
    self.__logs_tuple = a_logs_list, d_logs_list, g_logs_list
    return generative_model, discriminative_model