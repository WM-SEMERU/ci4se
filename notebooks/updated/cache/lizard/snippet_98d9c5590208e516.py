def draw(self):
    observed_arr = self.noise_sampler.generate()
    _ = self.inference(observed_arr)
    feature_arr = self.__convolutional_auto_encoder.extract_feature_points_arr(
        )
    for i in range(len(self.__deconvolution_layer_list)):
        try:
            feature_arr = self.__deconvolution_layer_list[i].forward_propagate(
                feature_arr)
        except:
            self.__logger.debug('Error raised in Deconvolution layer ' +
                str(i + 1))
            raise
    return feature_arr