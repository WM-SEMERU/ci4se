def vectorize(self, token_list):
    sentence_list = [token_list]
    test_observed_arr = self.__setup_dataset(sentence_list, self.
        __token_master_list)
    pred_arr = self.__controller.inference(test_observed_arr)
    return self.__controller.get_feature_points()