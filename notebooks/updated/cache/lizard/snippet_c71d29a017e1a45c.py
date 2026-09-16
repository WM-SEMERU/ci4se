def update(self):
    observed_arr = self.noise_sampler.generate()
    inferenced_arr = self.inference(observed_arr)
    error_arr = self.__encoder_decoder_controller.computable_loss.compute_loss(
        observed_arr, inferenced_arr)
    delta_arr = (self.__encoder_decoder_controller.computable_loss.
        compute_delta(observed_arr, inferenced_arr))
    decoder_grads_list, encoder_delta_arr, encoder_grads_list = (self.
        __encoder_decoder_controller.back_propagation(delta_arr))
    self.__encoder_decoder_controller.optimize(decoder_grads_list,
        encoder_grads_list, self.__learning_rate, 1)
    return error_arr